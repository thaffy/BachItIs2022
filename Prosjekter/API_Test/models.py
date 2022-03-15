from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

import database

class User(Base):
    __tablename__ = "User"

    userID = Column(String,primary_key=True,index=True)
    email = Column(String,index=True)
    password = Column(String,index=True)
    firstname = Column(String,index=True)
    lastname = Column(String,index=True)
    alias = Column(String,index=True)
    admin = Column(Boolean,index=True)
    country = Column(String,index=True)
