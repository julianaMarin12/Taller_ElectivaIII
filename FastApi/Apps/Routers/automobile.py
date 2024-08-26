from fastapi import APIRouter, Body
from Apps.models.automobile import Automobile


automobile_route = APIRouter()

@automobile_route.post("/")
def create_automobile (automobile:Automobile = Body(...)):
    try:
        return automobile
    except Exception as e:
        print(e)
        return {"error":str(e)}

@automobile_route.get("/{id}")
def guardar():
    return {"mensaje": "Guardado con éxito"}

@automobile_route.get("/{id}")
def get_automobile_by_id(id: int):
    return {"id": id}

@automobile_route.put("/{id}")
def update_automobile(id: int,automobile:Automobile = Body(...)):
    return {"id": id, "automobile": automobile}

@automobile_route.delete("/{id}")
def delete_automobile(id: int):
    return {"id": id}
