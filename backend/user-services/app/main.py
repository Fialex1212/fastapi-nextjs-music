from fastapi import FastAPI
from .api import users
from .api import auth
from db.init_db import lifespan

app = FastAPI(lifespan=lifespan)


app.include_router(users.router, prefix="/users")
app.include_router(auth.router, prefix="/auth")