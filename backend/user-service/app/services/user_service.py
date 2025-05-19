from db import crud
from models.schemas import UserCreate, UserOut
from models.models import User
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException, UploadFile
from app.utils.minio import minio_client
import os


ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


def create_user(user: UserCreate, db: Session) -> UserOut:
    return crud.create_user(user, db)


def get_user(user_id: int, db: Session) -> UserOut:
    return crud.get_user(user_id, db)


def get_user_by_email(email: str, db: Session) -> UserOut:
    return crud.get_user_by_email(email, db)


def get_users_list(db: Session) -> List[UserOut]:
    users = crud.get_users_list(db)
    return [UserOut.model_validate(user) for user in users]


def update_user_avatar(user_id: int, file: UploadFile, db: Session) -> UserOut:

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid content type. Allowed: {ALLOWED_CONTENT_TYPES}",
        )

    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400, detail=f"Invalid file type. Allowed: {ALLOWED_EXTENSIONS}"
        )

    user = crud.get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.avatar_key:
        minio_client.delete_avatar(user.avatar_key)

    try:
        avatar = minio_client.upload_avatar(
            file=file.file, user_id=user_id, file_extension=file_ext
        )
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=500, detail="Faild to upload avatar")

    updated_user = crud.update_user_avatar(db=db, user_id=user_id, avatar=avatar)

    return UserOut(
        id=updated_user.id,
        email=updated_user.email,
        username=updated_user.username,
        avatar_key=updated_user.avatar_key,
        avatar_url=minio_client.get_avatar_url(updated_user.avatar_key),
    )


def delete_user_avatar(user_id: int, db: Session) -> UserOut:
    user = crud.get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        if user.avatar_key:
            minio_client.delete_avatar(user.avatar_key)
            crud.update_user_avatar(db, user_id, None)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Faild to delete avatar")

    return user
