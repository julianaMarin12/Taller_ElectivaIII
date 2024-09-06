from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection
from Routers.user import user_route
from Routers.phone import phone_route
from Routers.house import house_route
from Routers.food import food_route
from Routers.automobile import automobile_route
from Routers.animal import animal_route

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
app.include_router(phone_route, prefix="/api/phone", tags=["phone"])
app.include_router(house_route, prefix="/api/house", tags=["house"])
app.include_router(food_route, prefix="/api/food", tags=["food"])
app.include_router(automobile_route, prefix="/api/auto", tags=["automobile"])
app.include_router(animal_route, prefix="/api/animal", tags=["animal"])
