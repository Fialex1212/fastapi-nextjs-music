from fastapi import FastAPI
from routers import user_proxy

app = FastAPI()

app.include_router(user_proxy.router, prefix="/api")

