from fastapi import APIRouter, Depends, UploadFile, File
from models.schemas import UserCreate, UserOut
from app.services.user_service import (
    create_user,
    get_user,
    get_user_by_email,
    get_users_list,
    update_user_avatar,
    delete_user_avatar,
)
from app.deps import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)


@router.get("/get_user_by_email", response_model=UserOut)
def get_user_by_email_route(email: str, db: Session = Depends(get_db)):
    return get_user_by_email(email, db)


@router.get("/users_list", response_model=List[UserOut])
def get_users_list_route(db: Session = Depends(get_db)):
    return get_users_list(db)


@router.get("/{user_id}", response_model=UserOut)
def get_user_route(user_id: int, db: Session = Depends(get_db)):
    return get_user(user_id, db)


@router.put("/{user_id}/avatar", response_model=UserOut)
def update_user_avatar_route(
    user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)
):
    return update_user_avatar(user_id, file, db)


@router.delete("/{user_id}/avatar", response_model=UserOut)
def delete_user_avatar_route(user_id: int, db: Session = Depends(get_db)):
    return delete_user_avatar(user_id, db)
