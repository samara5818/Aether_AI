from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserInDB(UserBase):
    hashed_password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class User(UserBase):
    id: int

class UserOut(BaseModel):
    id: int
    created_at: datetime
    email: EmailStr

    class Config:
        from_attributes = True
