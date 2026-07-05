from pydantic import BaseModel,EmailStr
from typing import Optional,List
from datetime import date

class CourseCreate(BaseModel):
          name:str
          code:str
          credits:int
          department_id:int

class CourseUpdate(BaseModel):
          name:Optional[str]=None
          code:Optional[str]=None
          credits:Optional[int]=None
          department_id:Optional[int]=None

class CourseResponse(CourseCreate):
          id:int
          class Config:
                    from_attributes=True

class DepartmentResponse(BaseModel):
          id:int
          name:str
          head_of_dept:str
          budget:int
          courses:List[CourseResponse]=[]
          
          class Config:
                    from_attributes=True

class StudentCreate(BaseModel):
          first_name: str
          last_name: str
          email: EmailStr
          department_id: Optional[int] = None
          enrollment_year: int
class StudentResponse(BaseModel):
          id:int
          first_name:str
          last_name:str
          email:str
          department_id:Optional[int]=None
          enrollment_year:int
          
          class Config:
                    from_attributes=True
                    

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

class UserCreate(BaseModel):
          email:EmailStr
          password:str 

class UserResponse(BaseModel):
          id:int
          email:EmailStr
          is_active:bool
          
          class Config:
                    from_attributes=True