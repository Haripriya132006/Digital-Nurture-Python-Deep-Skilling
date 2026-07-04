from fastapi import FastAPI,Depends,HTTPException,status
from typing import List,Optional
from schemas import CourseResponse,CourseCreate,CourseUpdate
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
app=FastAPI(title='Course Management API',version='1.0',lifespan=lifespan)

@app.get('/')
def view():
          return {'message':'API running'}

@app.post('/api/courses',response_model=CourseResponse)
async def create_courses(course:CourseCreate,db:AsyncSession=Depends(get_db)):
          db_course=models.Course(**course.model_dump())
          db.add(db_course)
          await db.commit()
          await db.refresh(db_course)
          return db_course

@app.get('/api/courses/',response_model=list[CourseResponse])
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
                    

@app.get("/api/courses/{course_id}",response_model=CourseResponse)
async def get_course(course_id:int,db:AsyncSession=Depends(get_db)):
          query=select(models.Course).where(models.Course.id==course_id)
          result=await db.execute(query)
          course=result.scalar_one_or_none()
          
          if course is None:
                    raise HTTPException(status_code=404,detail="Course not found")
          return course
