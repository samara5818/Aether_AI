from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserInDB(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
