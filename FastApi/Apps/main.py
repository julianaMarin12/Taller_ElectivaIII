from fastapi import FastAPI, Body
from Apps.models.food import Food
from Apps.models.user import User
from Apps.models.animal import Animal
from Apps.models.phone import Phone
from Apps.models.house import House
from Apps.models.automobile import Automobile
from starlette.responses import RedirectResponse
from contextlib import asynccontextmanager
from database import database as connection
from .Routers.user import user_route
from .Routers.food import food_route
from .Routers.animal import animal_route
from.Routers.phone import phone_route
from.Routers.house import house_route
from.Routers.automobile import automobile_route

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


@app.get("/")
def read_root():
    return {"Method": "GET"}

@app.post("/")
def read_root():
    return {"Method": "POST"}

@app.put("/")
def read_root():
    return {"Method": "PUT"}

@app.delete("/u")
def read_root():
    return {"Method": "DELETE"}



app.include_router(user_route, prefix="/users", tags=["Usuarios"])
app.include_router(food_route, prefix="/foods", tags=["Comida"])
app.include_router(animal_route, prefix="/animals", tags=["Mascotas"])
app.include_router(phone_route, prefix="/phone", tags=["Telefonos"])
app.include_router(house_route, prefix="/house", tags=["Casas"])
app.include_router(automobile_route, prefix="/automobile", tags=["Automovil"])