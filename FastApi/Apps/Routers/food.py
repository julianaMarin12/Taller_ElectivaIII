from fastapi import APIRouter, Body
from models.food import Food
from database import FoodModel 


food_route = APIRouter()

@food_route.post("/")
def create_food(food: Food = Body(...)):
    FoodModel.create(name= food.name, price =food.price, detail = food.detail)
    return {"message": "Food created successfully"}

@food_route.get("/")
def get_food():
    house = FoodModel.select().where(FoodModel.id_food > 0).dicts()
    return list(house)

@food_route.get("/{food_id}")
def get_food(food_id: int):
    try:
        food = FoodModel.get(FoodModel.id_food == food_id)
        return food
    except FoodModel.DoesNotExist:
        return {"error": "Food not found"}