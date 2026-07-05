from pydantic import BaseModel
from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException, status, Response, Request
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import declarative_base
from contextlib import asynccontextmanager

DATABASE_URL="sqlite+aiosqlite:///./course.db"

engine=create_async_engine(DATABASE_URL,echo=True)


AsyncSessionLocal=async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
)
Base=declarative_base()

async def get_db():
        async with AsyncSessionLocal() as session:
                yield session
# Assuming these come from your local database configuration file
@asynccontextmanager
async def lifespan(app:FastAPI):
        async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
        yield
app = FastAPI(title='Course Service',lifespan=lifespan)


# --- SQLAlchemy Models ---
class Course(Base):
        __tablename__ = "courses"
        
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, nullable=False)
        code = Column(String, nullable=False)
        credits = Column(Integer, nullable=False)
        department_id = Column(Integer, ForeignKey("departments.id", ondelete="SET NULL"), nullable=True)


# --- Pydantic Schemas ---
class CourseCreate(BaseModel):
        name: str
        code: str
        credits: int
        department_id: int

class CourseUpdate(BaseModel):
        name: Optional[str] = None
        code: Optional[str] = None
        credits: Optional[int] = None
        department_id: Optional[int] = None

class CourseResponse(CourseCreate):
        id: int
        class Config:
                from_attributes = True

class Department(Base):
        __tablename__="departments"
        id=Column(Integer,primary_key=True,index=True)
        name=Column(String,nullable=False)
        head_of_dept=Column(String,nullable=False)
        budget=Column(Integer,nullable=False)
        
class DepartmentResponse(BaseModel):
        id:int
        name:str
        head_of_dept:str
        budget:int
        courses:List[CourseResponse]=[]
        
        class Config:
                from_attributes=True
# --- API Routes ---

@app.post('/api/v1/courses',
        response_model=CourseResponse,
        status_code=status.HTTP_201_CREATED,
        tags=['Courses'],
        summary="Create new course",
        response_description="Course is successfully added")
async def create_courses(course: CourseCreate, response: Response, db: AsyncSession = Depends(get_db)):
        db_course = Course(**course.model_dump())
        db.add(db_course)
        await db.commit()
        await db.refresh(db_course)
        # Fixed URL structure to match your actual GET route
        response.headers['Location'] = f'/api/v1/courses/{db_course.id}'
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

        total_result=await db.execute(count_query)
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


@app.get("/api/v1/courses/{id}", response_model=CourseResponse, tags=['Courses'])
async def get_course(id: int, db: AsyncSession = Depends(get_db)):
    # Fixed: Removed models. prefix
        query = select(Course).where(Course.id == id)
        result = await db.execute(query)
        course = result.scalar_one_or_none()
    
        if course is None:
                    raise HTTPException(status_code=404, detail="Course not found")
        return course


@app.patch('/api/v1/courses/{id}', response_model=CourseResponse, tags=['Courses'])
async def update_course_part(id: int, course_data: CourseUpdate, db: AsyncSession = Depends(get_db)):
        query = select(Course).where(Course.id == id)
        result = await db.execute(query)
        db_course = result.scalar_one_or_none()

        if db_course is None:
                raise HTTPException(status_code=404, detail="Course not found")
        
        update_data = course_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
                setattr(db_course, key, value)
    
        await db.commit()
        await db.refresh(db_course)
        return db_course


@app.put('/api/v1/courses/{id}', response_model=CourseResponse, tags=['Courses'])
async def update_course(id: int, course_data: CourseCreate, db: AsyncSession = Depends(get_db)):
        query = select(Course).where(Course.id == id)
        result = await db.execute(query)
        db_course = result.scalar_one_or_none()

        if db_course is None:
                raise HTTPException(status_code=404, detail="Course not found")

        update_data = course_data.model_dump() # Includes all fields for a full replacement
        for key, value in update_data.items():
                setattr(db_course, key, value)

        await db.commit()
        await db.refresh(db_course)
        return db_course


@app.delete("/api/v1/courses/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Courses'])
async def delete_course(id: int, db: AsyncSession = Depends(get_db)):
        query = select(Course).where(Course.id == id)
        result = await db.execute(query)
        db_course = result.scalar_one_or_none()
        
        if db_course is None:
                raise HTTPException(status_code=404, detail="Course not found")
        await db.delete(db_course)
        await db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)