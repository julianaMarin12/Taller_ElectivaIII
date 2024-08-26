from fastapi import APIRouter, Body
from Apps.models.food import Food


food_route = APIRouter()

@food_route.post("/")
def create_food (food:Food = Body(...)):
    try:
        return food
    except Exception as e:
        print(e)
        return {"error":str(e)}

@food_route.get("/{id}")
def guardar():
    return {"mensaje": "Guardado con éxito"}

@food_route.get("/{id}")
def get_food_by_id(id: int):
    return {"id": id}

@food_route.put("/{id}")
def update_food(id: int,food:Food = Body(...)):
    return {"id": id, "food": food}


@food_route.delete("/{id}")
def delete_food(id: int):
    return {"id": id}