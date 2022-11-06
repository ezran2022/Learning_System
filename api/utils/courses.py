from sqlalchemy.orm import Session

from db.models.course import Course
from pydantic_schemas.course_control import CourseCreate


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session):
    return db.query(Course).all()