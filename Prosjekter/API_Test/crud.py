from sqlalchemy.orm import Session
import models
import schemas

def get_user(db : Session,userID: str):
    return db.query(models.User).filter(models.User.userID == userID).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()