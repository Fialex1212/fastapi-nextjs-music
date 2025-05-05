from db.session import engine, Base
from models.models import User
from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Создание таблиц...")
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы (или уже существуют).")
    
    yield
