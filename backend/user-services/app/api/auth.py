from fastapi import APIRouter, Depends
from models.schemas import UserLogin, UserWithToken, UserOut
from app.services.auth_service import login, get_current_user, logout
from app.services.user_service import get_user_by_email
from fastapi import HTTPException
from app.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login", response_model=UserWithToken)
def register_user(data: UserLogin, db: Session = Depends(get_db)):
    return login(data, db)

@router.post("/logout", response_model=UserOut)
def logout_router(token: str):
    return logout(token)

@router.get("/me", response_model=UserOut)
def get_me(email: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user = get_user_by_email(email, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user