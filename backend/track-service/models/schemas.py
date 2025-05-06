from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

# import uuid


class TrackCreate(BaseModel):
    title: str
    author_id: int


class TrackOut(BaseModel):
    id: int
    title: str
    author_id: int
    duration: Optional[str] = None
    cover_key: Optional[str] = None
    cover_url: Optional[str] = None
    track_key: Optional[str] = None
    track_url: Optional[str] = None

    class Config:
        from_attributes = True
