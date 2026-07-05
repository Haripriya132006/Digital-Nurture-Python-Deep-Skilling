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

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login/")

@app.get('/')
def view():
          return {'message':'API running'}










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
async def login(form_data:OAuth2PasswordRequestForm=Depends(),db:AsyncSession=Depends(get_db)):
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

