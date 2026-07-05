from sqlalchemy import Column,Integer,String,Date,ForeignKey
from database import Base

class Department(Base):
          __tablename__="departments"
          id=Column(Integer,primary_key=True,index=True)
          name=Column(String,nullable=False)
          head_of_dept=Column(String,nullable=False)
          budget=Column(Integer,nullable=False)
class Course(Base):
          __tablename__="courses"
          
          id=Column(Integer,primary_key=True,index=True)
          name=Column(String,nullable=False)
          code=Column(String,nullable=False)
          credits=Column(Integer,nullable=False)
          department_id=Column(Integer,ForeignKey("departments.id",ondelete="SET NULL"),nullable=True)

class Student(Base):
          __tablename__="students"
          id=Column(Integer,primary_key=True,index=True)
          first_name=Column(String,nullable=False)
          last_name=Column(String,nullable=False)
          email=Column(String,unique=True,nullable=False)
          department_id=Column(Integer,ForeignKey("departments.id",ondelete="SET NULL"),nullable=True)
          enrollment_year=Column(Integer,nullable=False)

class Enrollment(Base):
          __tablename__="enrollments"
          
          id=Column(Integer,primary_key=True,index=True)
          student_id=Column(Integer,ForeignKey("students.id",ondelete="CASCADE"),nullable=False)
          course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False) 
          enrollment_date=Column(Date,nullable=False)
          grade=Column(String,nullable=True)
          