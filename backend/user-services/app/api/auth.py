from fastapi import APIRouter, Depends
from models.schemas import UserLogin, UserWithToken, UserOut
from app.services.auth_service import login, get_current_user
from app.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login", response_model=UserWithToken)
def register_user(data: UserLogin, db: Session = Depends(get_db)):
    return login(data, db)

@router.post("/get_current_user", response_model=UserOut)
def get_current_user_route(token: str, db: Session = Depends(get_db)):
    return get_current_user(token, db)