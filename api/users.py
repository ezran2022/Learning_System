import fastapi
from fastapi import Depends, HTTPException
from typing import Optional, List
from db.db_setup import get_db
from pydantic_schemas.user_control import UserCreate, User
from api.utils.user import get_user, get_user_by_email, get_users, create_user
from sqlalchemy.orm import Session
router = fastapi.APIRouter()



@router.get("/users", response_model=List[User])
async def read_users(skip: int=0, limit: int=100, db:Session =Depends(get_db)):
    users= get_users(db, skip=skip, limit=limit)
    return users

@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user:UserCreate, db: Session=Depends(get_db)):
    db_user= get_user_by_email(db=db, email=user.email)
   # check if user is exist in db
    if db_user:
        raise HTTPException(status_code=404, detail="Email already registered")
    return create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session=Depends(get_db)):
    db_user= get_user(db=db, user_id=user_id)
   #check if user is available in db
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user  