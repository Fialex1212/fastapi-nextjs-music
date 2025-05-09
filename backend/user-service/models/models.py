from sqlalchemy import Column, String, Integer
from db.session import Base
# from sqlalchemy.dialects.postgresql import UUID
# import uuid

class User(Base):
    __tablename__ = "users"

    # id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    avatar_key = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
    hashed_password = Column(String)    