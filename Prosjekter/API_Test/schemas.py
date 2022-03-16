from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


## User-related classes
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


## Topic-related classes
class Topic(BaseModel):
    topicName: str
    topicID: int

    class Config:
        orm_mode = True

# Project-related classes
class Project(BaseModel):
    projectName: str
    projectID: int
    projectAdminUserID: int

    class Config:
        orm_mode = True