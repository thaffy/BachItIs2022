from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    userID: str
    firstname: str
    lastname: str
    alias : str
    admin: bool
    country: str

    class Config:
        orm_mode = True