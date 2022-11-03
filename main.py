from fastapi import FastAPI,Path, Query
from pydantic import BaseModel
from typing import Optional
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

users= []

class User(BaseModel):
    email:str
    is_active:bool
    bio:Optional[str]

@app.get("/users")
async def get_users():
    return users

@app.post("/users")
async def create_user(user:User):
    users.append(user)
    return "Successfully added new user"

@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The ID of user you want to retrieve ", gt=2),
    q: str = Query(None, max_length=5)
):
    return {"user":users[id], "query":q}