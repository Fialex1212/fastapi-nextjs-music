from fastapi import APIRouter, Depends
from models.schemas import UserLogin, UserWithToken, UserOut
from app.services.auth_service import login, get_current_user, logout
from app.services.user_service import get_user_by_email
from models.models import User
from fastapi import HTTPException
from app.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login", response_model=UserWithToken)
def login_user(data: UserLogin, db: Session = Depends(get_db)):
    return login(data, db)

@router.post("/logout", response_model=UserOut)
def logout_user(token: str):
    return logout(token)

@router.get("/me", response_model=UserOut)
def get_me(currect_user: User = Depends(get_current_user)):
    return currect_user

@router.get("/is_auth")
def is_auth(current_user: User = Depends(get_current_user)):
    return {"is_authenticated": True}