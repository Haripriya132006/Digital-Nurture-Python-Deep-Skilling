from sqlalchemy import Column,Integer,String,Date,ForeignKey,Boolean
from pydantic import BaseModel,EmailStr,ConfigDict
from typing import Optional,List
from datetime import date
from fastapi import FastAPI,Depends,HTTPException,status,Response,BackgroundTasks,Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import declarative_base,Session
from sqlalchemy.future import select
from contextlib import asynccontextmanager
import requests
import httpx

COURSE_SERVICE_URL = "http://localhost:5001/api/v1"  # Adjust to your course service URL

async def verify_course_exists(course_id: int) -> bool:
          async with httpx.AsyncClient() as client:
                    try:
                              response = await client.get(f"{COURSE_SERVICE_URL}/courses/{course_id}")
                              return response.status_code == 200
                    except httpx.RequestError:
                              raise HTTPException(
                              status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                              detail="Course service is currently unavailable"
                              )
                              
DATABASE_URL="sqlite+aiosqlite:///./student.db"

engine=create_async_engine(DATABASE_URL,echo=True)

AsyncSessionLocal=async_sessionmaker(
          bind=engine,
          class_=AsyncSession,
          expire_on_commit=False
)

@asynccontextmanager
async def lifespan(app:FastAPI):
          async with engine.begin() as conn:
                    await conn.run_sync(Base.metadata.create_all)
          yield
Base=declarative_base()

async def get_db():
          async with AsyncSessionLocal() as session:
                    yield session
                    
class Student(Base):
          __tablename__="students"
          id=Column(Integer,primary_key=True,index=True)
          first_name=Column(String,nullable=False)
          last_name=Column(String,nullable=False)
          email=Column(String,unique=True,nullable=False)
          department_id = Column(Integer, nullable=True)  
          enrollment_year=Column(Integer,nullable=False)

class StudentCreate(BaseModel):
          first_name: str
          last_name: str
          email: EmailStr
          department_id: Optional[int] = None
          enrollment_year: int
class StudentResponse(BaseModel):
          # Fixed: Modern Pydantic V2 configuration syntax
          model_config = ConfigDict(from_attributes=True)

          id: int
          first_name: str
          last_name: str
          email: str
          department_id: Optional[int] = None
          enrollment_year: int

class Enrollment(Base):
          __tablename__="enrollments"
          
          id=Column(Integer,primary_key=True,index=True)
          student_id=Column(Integer,nullable=False)
          course_id = Column(Integer, nullable=False)
          enrollment_date=Column(Date,nullable=False)
          grade=Column(String,nullable=True)

class EnrollmentCreate(BaseModel):
          student_id: int
          course_id: int
          enrollment_date: date
          grade: Optional[str] = None

class EnrollmentResponse(BaseModel):
          id:int
          student_id:int
          course_id:int
          enrollment_date:date
          grade:Optional[str]=None
          
          class Config:
                    from_attributes=True
                    
app=FastAPI(title='Student Service',lifespan=lifespan)

def send_confirmation_email(student_email: str):
          print(f"Sending confirmation to {student_email}")


@app.post("/api/v1/students/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED,tags=['Students'])
async def create_student(student: StudentCreate,response:Response, db: AsyncSession = Depends(get_db)):
          db_student = Student(**student.model_dump())
          db.add(db_student)
          await db.commit()
          await db.refresh(db_student)
          
          response.headers['Location']=f'/api/students/{db_student.id}/'
          
          return db_student

@app.delete("/api/v1/students/{id}", status_code=status.HTTP_204_NO_CONTENT,tags=['Students'])
async def delete_student(id: int, db: AsyncSession = Depends(get_db)):
          query = select(Student).where(Student.id == id)
          result = await db.execute(query)
          db_student = result.scalar_one_or_none()
          if not db_student:
                    raise HTTPException(status_code=404, detail="Student not found")
          await db.delete(db_student)
          await db.commit()
          return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.post("/api/v1/enrollments",response_model=EnrollmentResponse,status_code=status.HTTP_201_CREATED,tags=['Enrollment'])
async def create_enrollment(enrollment:EnrollmentCreate,background_tasks:BackgroundTasks,response:Response,db:AsyncSession=Depends(get_db)):
          
          student_query=select(Student).where(Student.id == enrollment.student_id)
          student_result=await db.execute(student_query)
          student=student_result.scalar_one_or_none()
          
          if not student:
                    raise HTTPException(status_code=404,detail="Student not found")
          
          course_exists=await verify_course_exists(enrollment.course_id)
          
          if not course_exists:
                    raise HTTPException(status_code=404,detail="Course not found in Course Service")
          
          db_enrollment = Enrollment(**enrollment.model_dump())
          db.add(db_enrollment)
          await db.commit()
          await db.refresh(db_enrollment)
          
          response.headers['Location']=f'/api/enrollments/{db_enrollment.id}/'
          
          background_tasks.add_task(send_confirmation_email,student.email)
          return db_enrollment


@app.get("/api/v1/courses/{id}/students/",response_model=List[StudentResponse],tags=['Courses'])
async def get_course_students(id:int,db:AsyncSession=Depends(get_db)):

          course_exists=(await verify_course_exists(id))
          if not course_exists:
                    raise HTTPException(status_code=404,detail="Course not found in Course Service")
          
          query=(
                    select(Student)
                    .join(Enrollment,Student.id==Enrollment.student_id)
                    .where(Enrollment.course_id==id)
          )
          result=await db.execute(query)
          students=result.scalars().all()
          return students
