from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import Request
from starlette.responses import Response

from app.auth.controller.AuthController import auth
from app.db.db import metadata, engine, database

metadata.create_all(engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title="E PAAS",
    description="This is a very fancy project",
    version="0.1.0",
)


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        # you probably want some kind of logging here
        return Response("Internal server error", status_code=500)


app.middleware('http')(catch_exceptions_middleware)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(auth)
