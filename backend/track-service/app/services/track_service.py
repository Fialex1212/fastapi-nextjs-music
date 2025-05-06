from db import crud
from models.schemas import TrackCreate, TrackOut
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException, UploadFile
import os


def create_track(track: TrackCreate, track_file: UploadFile, db: Session):
    return crud.create_track(track=track, track_file=track_file, db=db)


def get_track(track_id: int, db: Session) -> TrackOut:
    return crud.get_track(track_id, db)
