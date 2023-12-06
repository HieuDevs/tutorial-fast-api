from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class UserPost(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Post(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = True
    created_at: Optional[datetime] = None
    owner_id: Optional[int] = None
    owner: Optional[UserPost] = None

    class Config:
        from_attributes: True
