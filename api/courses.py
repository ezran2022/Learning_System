import fastapi
from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic_schemas.course_control import Course, CourseCreate
from api.utils.courses import get_course, get_courses, create_course
router= fastapi.APIRouter()


@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses

@router.post("/courses")
async def create_new_course(course:Course):
    courses.append(course)
    return "Successfully added new course"

@router.get("/courses/{id}")
async def read_course(id: int):
    return {"user":courses[id]}

@router.patch("/courses/{id}")
async def update_course(id: int):
    return {"user":courses[id]}

@router.delete("/courses/{id}")
async def delete_course(id: int):
    return {"user":courses[id]}
