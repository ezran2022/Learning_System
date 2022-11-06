from fastapi import FastAPI
from api import users, sections, courses
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Learning System",
    description="System for managing students and courses",
    version="0.1.0",
    contact={
        "name":"Ezraa OG",
        "email":"ntwaribusiness@gmail.com"
    },
    license_info={
        "name":"ENSolution LTD"
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)

