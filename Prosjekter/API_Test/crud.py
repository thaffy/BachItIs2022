from sqlalchemy.orm import Session
import models
import schemas

## User-related functions
def get_user(db : Session,userID: int):
    return db.query(models.User).filter(models.User.userID == userID).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# Topic-related functions
def get_topic(db: Session,topicID: int):
    return db.query(models.Topic).filter(models.Topic.topicID == topicID).first()

def get_topic_by_name(db: Session,topicName: str):
    return db.query(models.Topic).filter(models.Topic.topicName == topicName).first()

def get_topics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Topic).offset(skip).limit(limit).all()

