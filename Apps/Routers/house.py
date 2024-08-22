from fastapi import APIRouter, Body
from Apps.models.house import House


house_route = APIRouter()

@house_route.post("/")
def create_house (house:House = Body(...)):
    try:
        return house
    except Exception as e:
        print(e)
        return {"error":str(e)}

@house_route.get("/{id}")
def guardar():
    return {"mensaje": "Guardado con éxito"}

@house_route.get("/{id}")
def get_house_by_id(id: int):
    return {"id": id}

@house_route.put("/{id}")
def update_house(id: int,house:House = Body(...)):
    return {"id": id, "house": house}

@house_route.delete("/{id}")
def delete_house(id: int):
    return {"id": id}