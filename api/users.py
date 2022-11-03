import fastapi
from pydantic import BaseModel
from typing import Optional
router = fastapi.APIRouter()

users= []

class User(BaseModel):
    email:str
    is_active:bool
    bio:Optional[str]

@router.get("/users")
async def get_():
    return users

@router.post("/users")
async def create_user(user:User):
    users.append(user)
    return "Successfully added new user"

@router.get("/users/{id}")
async def get_user(id: int):
    return {"user":users[id]}    