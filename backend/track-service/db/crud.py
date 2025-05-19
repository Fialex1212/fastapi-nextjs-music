from models.schemas import TrackCreate, TrackOut
from models.models import Track
from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException, UploadFile
from app.utils.minio_tracks import minio_track_client
from app.utils.minio_covers import minio_cover_client
from app.utils.generate_cover import generate_cover
import io


def create_track(track: TrackCreate, track_file: UploadFile, db: Session):
    db_track = db.query(Track).filter(Track.title == track.title).first()
    if db_track:
        raise HTTPException(status_code=400, detail="Title already took")

    new_track = Track(
        title=track.title,
        author_id=track.author_id,
    )

    db.add(new_track)
    db.commit()
    db.refresh(new_track)

    # Upload Cover
    try:
        cover_bytes, _ = generate_cover(new_track.title)
        file_obj = io.BytesIO(cover_bytes)
        file_ext = ".png"
        cover_key = minio_cover_client.upload_track_cover(
            file=file_obj,
            track_id=new_track.id,
            track_title=new_track.title,
            file_extension=file_ext,
        )
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=500, detail="Faild to upload cover")

    # Upload Track
    try:
        track_ext = f".{track_file.filename.split('.')[-1]}"
        track_key = minio_track_client.upload_track(
            file=track_file.file,
            track_id=new_track.id,
            track_title=new_track.title,
            file_extension=".mp3",
        )
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=500, detail="Failed to upload track file")

    update_cover(track_id=new_track.id, db=db, cover_key=cover_key)
    update_track_key(db=db, track_id=new_track.id, track_key=track_key)

    updated_track = db.query(Track).filter(Track.id == new_track.id).first()

    return TrackOut(
        id=updated_track.id,
        title=updated_track.title,
        author_id=updated_track.author_id,
        duration=updated_track.duration,
        cover_key=updated_track.cover_key,
        cover_url=minio_cover_client.get_track_cover_url(updated_track.cover_key),
        track_key=updated_track.track_key,
        track_url=minio_track_client.get_track_url(updated_track.track_key),
    )


def get_track(track_id: int, db: Session):
    db_track = db.query(Track).filter(Track.id == track_id).first()
    if not db_track:
        raise HTTPException(status_code=404, detail="Track not found")
    return TrackOut(
        id=db_track.id,
        title=db_track.title,
        author_id=db_track.author_id,
        duration=db_track.duration,
        cover_key=db_track.cover_key,
        cover_url=minio_cover_client.get_track_cover_url(db_track.cover_key),
        track_key=db_track.track_key,
        track_url=minio_track_client.get_track_url(db_track.track_key),
    )


def get_tracks(db: Session):
    pass


def update_track(track_id: int, db: Session):
    pass


def delete_track(track_id: int, db: Session):
    pass


def update_cover(track_id: int, db: Session, cover_key: str):
    db_track = get_track(track_id, db)
    if not db_track:
        raise HTTPException(status_code=404, detail="Track not found")
    db_track.cover_key = cover_key
    db.commit()
    db.refresh(db_track)
    return db_track


def update_track_key(db: Session, track_id: int, track_key: str):
    db_track = get_track(track_id, db)
    if not db_track:
        raise HTTPException(status_code=404, detail="Track not found")
    db_track.track_key = track_key
    db.commit()
    db.refresh(db_track)
    return db_track
