from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine("postgresql://user:password@postgresql:5432/musicdb")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
