from fastapi import FastAPI, Body
from models.food import Food
from models.user import User
from models.animal import Animal
from models.automobile import Automobile
from models.phone import Phone
from  starlette.responses import RedirectResponse
from Routers.user import user_route
from Routers.food import food_route
from Routers.animal import animal_route
from Routers.phone import phone_route
from Routers.automobile import automobile_route


app = FastAPI()


app.include_router(user_route, prefix="/users", tags=["Usuarios"])
app.include_router(food_route, prefix="/foods", tags=["Comida"])
app.include_router(animal_route, prefix="/animals", tags=["Mascotas"])
app.include_router(phone_route, prefix="/phone", tags=["Telefonos"])
app.include_router(automobile_route, prefix="/automobile",tags=["automobiles"])
