from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from app.utils.minio import minio_client

# import uuid


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    avatar_key: Optional[str] = None
    avatar_url: Optional[str] = None

    @property
    def avatar_url(self):
        if self.avatar_url:
            return minio_client.get_avatar_url(self.avatar_key)
        return None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str


class UserWithToken(UserOut):
    access_token: str
