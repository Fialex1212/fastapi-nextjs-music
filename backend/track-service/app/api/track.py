from fastapi import APIRouter, Depends, UploadFile, File, Form
from models.schemas import TrackCreate, TrackOut
from app.services.track_service import create_track, get_track
from app.deps import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()


@router.post("/")
async def create_track_route(
    track_data: TrackCreate = Depends(),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    return create_track(track_data, file, db)


# @router.get("/users_list", response_model=List[UserOut])
# def get_users_list_route(db: Session = Depends(get_db)):
#     return get_users_list(db)


@router.get("/{track_id}", response_model=TrackOut)
def get_user_route(track_id: int, db: Session = Depends(get_db)):
    return get_track(track_id, db)
