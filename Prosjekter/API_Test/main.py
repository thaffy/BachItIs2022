# uvicorn main:app --reload
# python -m uvicorn main:app --reload
# for å teste API i localhost...
from typing import List

from fastapi import Depends,FastAPI, Request, HTTPException

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
    
@app.get("/public.Users/{userID}", response_model=schemas.User)
def read_user(userID: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, userID=userID)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/public.Users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
