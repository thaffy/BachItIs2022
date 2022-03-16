
from sqlalchemy import CHAR, TEXT, TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

import database

class User(Base):
    __tablename__ = "User"

    email = Column(String,index=True)
    password = Column(TEXT,index=True)
    firstName = Column(String,index=True)
    lastName = Column(String,index=True)
    alias = Column(String,index=True)
    admin = Column(Boolean,index=True)
    countryID = Column(CHAR,index=True)
    userID = Column(Integer,primary_key=True,index=True)
    timestamp = Column(TIMESTAMP,index=True)

class Topic(Base):
    __tablename__ = "Topic"

    topicID = Column(Integer,primary_key=True,index=True)
    topicName = Column(String,index=True)

class ForumPost(Base):
    __tablename__ = "ForumPost"

    forumPostID = Column(Integer,primary_key=True,index=True)
    userID = Column(Integer,index=True)
    text = Column(String,index=True)
    forumPostFileID = Column(Integer,index=True)
    timestamp = Column(TIMESTAMP,index=True)
    
