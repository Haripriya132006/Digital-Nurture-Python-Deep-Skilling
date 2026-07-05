from fastapi import FastAPI,Depends,HTTPException,status,Response,BackgroundTasks
from typing import List,Optional
from schemas import CourseResponse,CourseCreate,CourseUpdate,EnrollmentCreate,EnrollmentResponse,StudentResponse,StudentCreate
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db,Base,engine
import models
from models import Course
from sqlalchemy.future import select
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
          async with engine.begin() as conn:
                    await conn.run_sync(Base.metadata.create_all)
          yield
def send_confirmation_email(student_email: str):
          print(f"Sending confirmation to {student_email}")

app=FastAPI(title='Course Management API',version='1.0',description='API for university Courses',contact={"name":"Haripriya","email":"haripriya@test.com"},lifespan=lifespan)

@app.get('/')
def view():
          return {'message':'API running'}


@app.post('/api/courses',
          response_model=CourseResponse,
          status_code=status.HTTP_201_CREATED,
          tags=['Courses'],
          summary="Create new course",
          response_description="Course is successfully added")

async def create_courses(course:CourseCreate,db:AsyncSession=Depends(get_db)):
          db_course=models.Course(**course.model_dump())
          db.add(db_course)
          await db.commit()
          await db.refresh(db_course)
          return db_course

@app.get('/api/courses/',response_model=list[CourseResponse],tags=['Courses'])
async def get_courses(
          skip:int=0,
          limit:int=10,
          department_id:Optional[int]=None,
          db:AsyncSession=Depends(get_db)):
          
          query=select(Course)
          if(department_id is not None):
                    query=query.where(Course.department_id==department_id)
                    
          query=query.offset(skip).limit(limit)
                    
          result=await db.execute(query)
          courses=result.scalars().all()
          return courses if courses is not None else []
                    

@app.get("/api/courses/{course_id}",response_model=CourseResponse,tags=['Courses'])
async def get_course(course_id:int,db:AsyncSession=Depends(get_db)):
          query=select(models.Course).where(models.Course.id==course_id)
          result=await db.execute(query)
          course=result.scalar_one_or_none()
          
          if course is None:
                    raise HTTPException(status_code=404,detail="Course not found")
          return course

# newly added

@app.get('/api/courses/{id}',response_model=CourseResponse,tags=['Courses'])
async def update_course(id:int,course_data:CourseUpdate,db:AsyncSession=Depends(get_db)):
          query=select(models.Course).where(models.Course.id==course_id)
          result=await db.execute(query)
          db_course=result.scalar_one_or_none()
          
          if db_course is None:
                    raise HTTPException(status_code=404,detail="Course not found")
          update_data=course_data.model_dump(exclude_unset=True)
          for key,value in update_data.items():
                    setattr(db_course,key,value)
          await db.commit()
          await db.refresh(db_course)
          return db_course

@app.delete("/api/courses/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=['Courses'])
async def delete_course(id:int,db:AsyncSession=Depends(get_db)):
          query=select(Course).where(Course.id==id)
          result=await db.execute(query)
          db_course=result.scalar_one_or_none()
          
          if db_course is None:
                    raise HTTPException(status_code=404,detail="Course not found")
          await db.delete(db_course)
          await db.commit()
          return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.post("/api/enrollments",response_model=EnrollmentResponse,status_code=status.HTTP_201_CREATED,tags=['Enrollment'])
async def create_enrollment(enrollment:EnrollmentCreate,background_tasks:BackgroundTasks,db:AsyncSession=Depends(get_db)):
          
          student_query=select(models.Student).where(models.Student.id == enrollment.student_id)
          student_result=await db.execute(student_query)
          student=student_result.scalar_one_or_none()
          
          if not student:
                    raise HTTPException(Status_code=404,detail="Student not found")
          
          db_enrollment = models.Enrollment(**enrollment.model_dump())
          db.add(db_enrollment)
          await db.commit()
          await db.refresh(db_enrollment)
          
          background_tasks.add_task(send_confirmation_email,student.email)
          return db_enrollment

@app.post("/api/students/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED,tags=['Students'])
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
          db_student = models.Student(**student.model_dump())
          db.add(db_student)
          await db.commit()
          await db.refresh(db_student)
          return db_student

@app.delete("/api/students/{id}", status_code=status.HTTP_204_NO_CONTENT,tags=['Students'])
async def delete_student(id: int, db: AsyncSession = Depends(get_db)):
          query = select(models.Student).where(models.Student.id == id)
          result = await db.execute(query)
          db_student = result.scalar_one_or_none()
          if not db_student:
                    raise HTTPException(status_code=404, detail="Student not found")
          await db.delete(db_student)
          await db.commit()
          return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/api/courses/{id}/students/",response_model=List[StudentResponse],tags=['Courses'])
async def get_course_students(id:int,db:AsyncSession=Depends(get_db)):
          course_query=select(models.Course).where(models.Course.id==id)
          course_exists=(await db.execute(course_query)).scalar_one_or_none()
          if not course_exists:
                    raise HTTPException(status_code=404,detail="Course not found")
          
          query=(
                    select(models.Student)
                    .join(models.Enrollment,models.Student.id==models.Enrollment.student_id)
                    .where(models.Enrollment.course_id==id)
          )
          result=await db.execute(query)
          students=result.scalars().all()
          return students