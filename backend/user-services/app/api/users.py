from fastapi import APIRouter, Depends
from models.schemas import UserCreate, UserOut
from app.services.user_service import create_user, get_user, get_user_by_email
from app.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)

@router.get("/get_user", response_model=UserOut)
def get_user_route(user_id: int, db: Session = Depends(get_db)):
    return get_user(user_id, db)

@router.get("/get_user_by_email", response_model=UserOut)
def get_user_by_email_route(email: str, db: Session = Depends(get_db)):
    return get_user_by_email(email, db)