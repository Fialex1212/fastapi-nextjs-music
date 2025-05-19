from models.models import User
from models.schemas import UserOut
from sqlalchemy.orm import Session
from models.schemas import UserCreate
from app.utils.security import hash_password
from fastapi import HTTPException
from app.utils.minio import minio_client
from app.utils.generate_avatar import generate_avatar
import io


def create_user(user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    try:
        avatar_bytes, filename = generate_avatar(user.username)
        file_obj = io.BytesIO(avatar_bytes)
        file_ext = ".png"
        avatar_key = minio_client.upload_avatar(
            file=file_obj, user_id=new_user.id, file_extension=file_ext
        )
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=500, detail="Faild to upload avatar")

    updated_user = update_user_avatar(db=db, user_id=new_user.id, avatar=avatar_key)

    return UserOut(
        id=updated_user.id,
        email=updated_user.email,
        username=updated_user.username,
        avatar_key=updated_user.avatar_key,
        avatar_url=minio_client.get_avatar_url(updated_user.avatar_key),
    )


def get_user(user_id: str, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    avatar_url = None
    if user.avatar_key:
        avatar_url = minio_client.get_avatar_url(user.avatar_key)
    return UserOut(
        id=user.id,
        email=user.email,
        username=user.username,
        avatar_key=user.avatar_key,
        avatar_url=avatar_url,
    )


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    avatar_url = None
    if user.avatar_key:
        avatar_url = minio_client.get_avatar_url(user.avatar_key)
    return UserOut(
        id=user.id,
        email=user.email,
        username=user.username,
        avatar_key=user.avatar_key,
        avatar_url=avatar_url,
    )



def get_users_list(db: Session):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users


def update_user_avatar(db: Session, user_id: int, avatar: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.avatar_key = avatar
    db.commit()
    db.refresh(user)
    return user
