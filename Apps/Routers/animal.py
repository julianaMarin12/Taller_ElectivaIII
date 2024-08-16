from fastapi import APIRouter, Body
from Apps.models.animal import Animal


animal_route = APIRouter()

@animal_route.post("/")
def create_animal (animal:Animal = Body(...)):
    try:
        return animal
    except Exception as e:
        print(e)
        return {"error":str(e)}

@animal_route.get("/{id}")
def guardar():
    return {"mensaje": "Guardado con éxito"}

@animal_route.get("/{id}")
def get_animal_by_id(id: int):
    return {"id": id}

@animal_route.put("/{id}")
def update_animal(id: int,animal:Animal = Body(...)):
    return {"id": id, "animal": animal}
