from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection
from Routers.user import user_route

@asynccontextmanager
async def lifespam(app: FastAPI):

    if(connection.is_closed()):
        connection.connect()

    try:
        yield

    finally:
        if not (connection.is_closed()):
            connection.close()

app = FastAPI(lifespan = lifespam)

app.include_router(user_route, prefix="/api/users", tags=["users"])