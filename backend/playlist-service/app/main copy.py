from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from .api import track
from db.init_db import lifespan

app = FastAPI(lifespan=lifespan)

app.include_router(track.router, prefix="/track", tags=["Track"])