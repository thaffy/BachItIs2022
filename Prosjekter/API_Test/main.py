# uvicorn main:app --reload
# python -m uvicorn main:app --reload
# for å teste API i localhost...
from typing import List, Optional

from fastapi import Depends,FastAPI, Request, HTTPException, Query

from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
# Søker etter bruker via userID
@app.get("/user/{UserID}", response_model=schemas.User)
def read_user(userID: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, userID=userID)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Søker opp bruker via email
@app.get("/user/{Email}", response_model=schemas.User)
def read_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Søker opp alle brukere i en liste
@app.get("/user/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users



# Søker opp topic via topicID
@app.get("/topic/{TopicID}", response_model=schemas.Topic)
def read_topic(topicID: int, db: Session = Depends(get_db)):
    db_topic = crud.get_topic(db, topicID=topicID)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic

# Søker opp topic via topicName
@app.get("/topic/{TopicName}", response_model=schemas.Topic)
def read_topic(topicName: str, db: Session = Depends(get_db)):
    db_topic = crud.get_topic_by_name(db, topicName=topicName)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic

# Søker opp alle topics i en liste
@app.get("/topic/",response_model=List[schemas.Topic])
def read_topics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    topics = crud.get_topics(db, skip=skip, limit=limit)
    return topics
