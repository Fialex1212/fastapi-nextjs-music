from sqlalchemy import Column, Integer, String
from db.session import Base


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=True)
    track_key = Column(String, nullable=True)
    track_url = Column(String, nullable=True)
    cover_key = Column(String, nullable=True)
    cover_url = Column(String, nullable=True)
