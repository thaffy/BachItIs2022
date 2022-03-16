from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    
    password: str
    firstName: str
    lastName: str
    alias : str
    admin: bool
    countryID: int
    userID: int
    timestamp: datetime

    class Config:
        orm_mode = True