import fastapi
from typing import Optional
from pydantic import BaseModel
router= fastapi.APIRouter()

courses= []

class Course(BaseModel):
    Subject:str
    bio:Optional[str]

@router.get("/courses")
async def get_courses():
    return courses

@router.post("/courses")
async def create_course(course:Course):
    courses.append(course)
    return "Successfully added new course"

@router.get("/courses/{id}")
async def get_course(id: int):
    return {"user":courses[id]}

@router.patch("/courses/{id}")
async def update_course(id: int):
    return {"user":courses[id]}

@router.delete("/courses/{id}")
async def delete_course(id: int):
    return {"user":courses[id]}
