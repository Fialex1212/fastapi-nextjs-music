from db import crud
from models.schemas import UserCreate, UserOut
from sqlalchemy.orm import Session

def create_user(user: UserCreate, db: Session) -> UserOut:
    return crud.create_user(user, db)

def get_user(user_id: int, db: Session) -> UserOut:
    return crud.get_user(user_id, db)

def get_user_by_email(email: str, db: Session) -> UserOut:
    return crud.get_user_by_email(email, db)