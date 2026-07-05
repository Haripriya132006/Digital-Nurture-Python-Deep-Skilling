from fastapi import FastAPI,Depends,HTTPException,status,Response,BackgroundTasks,Request
from typing import List,Optional
from schemas import *
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db,Base,engine
import models
from models import Course
from sqlalchemy.future import select
from contextlib import asynccontextmanager
from sqlalchemy import func
from security import get_password_hash,verify_password,create_access_token,SECRET_KEY,ALGORITHM
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError

@asynccontextmanager
async def lifespan(app:FastAPI):
          async with engine.begin() as conn:
                    await conn.run_sync(Base.metadata.create_all)
          yield
def send_confirmation_email(student_email: str):
          print(f"Sending confirmation to {student_email}")

app=FastAPI(title='Course Management API',version='1.0',description='API for university Courses',contact={"name":"Haripriya","email":"haripriya@test.com"},lifespan=lifespan)

origins=[
          "http://localhost:3000" #react frontend
]
app.add_middleware(
          CORSMiddleware,
          allow_origins=origins,
          allow_credentials=True,
          allow_methods=["*"],
          allow_headers=["*"],
)

oauth2_scheme=OAuth2PasswordBearer(token_Url="/api/v1/auth/login/")

@app.get('/')
def view():
          return {'message':'API running'}


@app.post('/api/v1/courses',
          response_model=CourseResponse,
          status_code=status.HTTP_201_CREATED,
          tags=['Courses'],
          summary="Create new course",
          response_description="Course is successfully added")
async def create_courses(course:CourseCreate,response:Response,db:AsyncSession=Depends(get_db)):
          db_course=models.Course(**course.model_dump())
          db.add(db_course)
          await db.commit()
          await db.refresh(db_course)
          response.headers['Location']=f'/api/courses/{db_course.id}/'
          return db_course

@app.get('/api/v1/courses/', tags=['Courses'])
async def get_pages(
          request: Request,
          page: int = 1,
          page_size: int = 10,
          department_id: Optional[int] = None,
          search: Optional[str] = None,
          db: AsyncSession = Depends(get_db)
          ):
          if page < 1:
                    page = 1
          if page_size < 1:
                    page_size = 10

          query = select(Course)
          count_query = select(func.count()).select_from(Course)

          if department_id is not None:
                    query = query.where(Course.department_id == department_id)
                    count_query = count_query.where(Course.department_id == department_id)

          if search:
                    search_filter = Course.name.ilike(f"%{search}%") | Course.code.ilike(f"%{search}%")
                    query = query.where(search_filter)
                    count_query = count_query.where(search_filter)

          total_result = await db.execute(count_query)
          total_count = total_result.scalar_one()

          offset_value = (page - 1) * page_size
          query = query.offset(offset_value).limit(page_size)

          result = await db.execute(query)
          courses = result.scalars().all()

          base_url = str(request.url.remove_query_params(["page", "page_size"]))
          
          next_url = None
          if offset_value + page_size < total_count:
                    next_url = f"{base_url}?page={page + 1}&page_size={page_size}"
                    if department_id: next_url += f"&department_id={department_id}"
                    if search: next_url += f"&search={search}"

          previous_url = None
          if page > 1:
                    previous_url = f"{base_url}?page={page - 1}&page_size={page_size}"
                    if department_id: previous_url += f"&department_id={department_id}"
                    if search: previous_url += f"&search={search}"

          return {
                    "count": total_count,
                    "next": next_url,
                    "previous": previous_url,
                    "results": courses
          }

@app.get("/api/v1/courses/{id}",response_model=CourseResponse,tags=['Courses'])
async def get_course(id:int,db:AsyncSession=Depends(get_db)):
          query=select(models.Course).where(models.Course.id==id)
          result=await db.execute(query)
          course=result.scalar_one_or_none()
          
          if course is None:
                    raise HTTPException(status_code=404,detail="Course not found")
          return course

# newly added
@app.patch('/api/v1/courses/{id}',response_model=CourseResponse,tags=['Courses'])
async def update_course_part(id:int,course_data:CourseUpdate,db:AsyncSession=Depends(get_db)):
          query=select(models.Course).where(models.Course.id==id)
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

@app.put('/api/v1/courses/{id}',response_model=CourseResponse,tags=['Courses'])
async def update_course(id:int,course_data:CourseUpdate,db:AsyncSession=Depends(get_db)):
          query=select(models.Course).where(models.Course.id==id)
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

@app.delete("/api/v1/courses/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=['Courses'])
async def delete_course(id:int,db:AsyncSession=Depends(get_db)):
          query=select(Course).where(Course.id==id)
          result=await db.execute(query)
          db_course=result.scalar_one_or_none()
          
          if db_course is None:
                    raise HTTPException(status_code=404,detail="Course not found")
          await db.delete(db_course)
          await db.commit()
          return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.post("/api/v1/enrollments",response_model=EnrollmentResponse,status_code=status.HTTP_201_CREATED,tags=['Enrollment'])
async def create_enrollment(enrollment:EnrollmentCreate,background_tasks:BackgroundTasks,response:Response,db:AsyncSession=Depends(get_db)):
          
          student_query=select(models.Student).where(models.Student.id == enrollment.student_id)
          student_result=await db.execute(student_query)
          student=student_result.scalar_one_or_none()
          
          if not student:
                    raise HTTPException(status_code=404,detail="Student not found")
          
          course_query=select(models.Course).where(models.Course.id == enrollment.course_id)
          course_result=await db.execute(course_query)
          course=course_result.scalar_one_or_none()
          
          if not course:
                    raise HTTPException(status_code=404,detail="Course not found")
          
          db_enrollment = models.Enrollment(**enrollment.model_dump())
          db.add(db_enrollment)
          await db.commit()
          await db.refresh(db_enrollment)
          
          response.headers['Location']=f'/api/enrollments/{db_enrollment.id}/'
          
          background_tasks.add_task(send_confirmation_email,student.email)
          return db_enrollment

@app.post("/api/v1/students/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED,tags=['Students'])
async def create_student(student: StudentCreate,response:Response, db: AsyncSession = Depends(get_db)):
          db_student = models.Student(**student.model_dump())
          db.add(db_student)
          await db.commit()
          await db.refresh(db_student)
          
          response.headers['Location']=f'/api/students/{db_student.id}/'
          
          return db_student

@app.delete("/api/v1/students/{id}", status_code=status.HTTP_204_NO_CONTENT,tags=['Students'])
async def delete_student(id: int, db: AsyncSession = Depends(get_db)):
          query = select(models.Student).where(models.Student.id == id)
          result = await db.execute(query)
          db_student = result.scalar_one_or_none()
          if not db_student:
                    raise HTTPException(status_code=404, detail="Student not found")
          await db.delete(db_student)
          await db.commit()
          return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/api/v1/courses/{id}/students/",response_model=List[StudentResponse],tags=['Courses'])
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

@app.post("/api/v1/auth/register/",response_model=UserResponse,
          status_code=status.HTTP_201_CREATED,
          tags=['Authentication'])
async def register_user(user_data:UserCreate,db:AsyncSession=Depends(get_db)):
          query=select(models.User).where(models.User.email ==user_data.email)
          result=await db.execute(query)
          existing_user=result.scalar_one_or_none()
          
          if (existing_user):
                    raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Email is already registered")
          hashed=get_password_hash(user_data.password)
          print(f"🔒 HASHED PASSWORD GOING TO DB: {hashed}")
          print("="*50 + "\n")
          new_user=models.User(email=user_data.email,hashed_password=hashed,is_active=True)
          
          db.add(new_user)
          await db.commit()
          await db.refresh(new_user)
          
          return new_user

async def get_current_user(token:str=Depends(oauth2_scheme),db:AsyncSession=Depends(get_db)):
          credentials_exception=HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate":"Bearer"},
          )
          try:
                    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
                    email:str=payload.get("sub")
                    if email is None:
                              raise credentials_exception
          except JWTError:
                    raise credentials_exception
          query=select(models.User).where(models.User.email==email)
          result=await db.execute(query)
          user=result.scalar_one_or_none()
          
          if user is None:
                    raise credentials_exception
          return user
                    

@app.post("/api/v1/auth/login/",tags=["Authentication"])
async def login(form_data:OAuth2PasswordRequestForm=Depends,db:AsyncSession=Depends(get_db)):
          query=select(models.User).where(models.User.email==form_data.username)
          result=await db.execute(query)
          user=result.scalar_one_or_none()
          
          if not user or not verify_password(form_data.password,user.hashed_password):
                    raise HTTPException(
                              status_code=status.HTTP_401_UNAUTHORIZED,
                              detail="Incorrect email or password",
                              headers={"WWW-Authenticate":"Bearer"},
                    )
          access_token=create_access_token(data={"sub":user.email})
          return {"access_token":access_token,"token_type":"bearer"}

@app.post("/api/v2/courses/")
async def create_courses(course_data: dict, current_user: models.User = Depends(get_current_user)):
          return {"message": "Course created successfully", "by_user": current_user.email}

@app.delete("/api/v2/courses/{course_id}")
async def delete_courses(course_id: int, current_user: models.User = Depends(get_current_user)):
          return {"message": f"Course {course_id} deleted successfully"}

