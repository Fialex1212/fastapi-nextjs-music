from fastapi import FastAPI
from db.init_db import lifespan

app = FastAPI(lifespan=lifespan)