from fastapi import APIRouter, Body
from Apps.models.phone import Phone


phone_route = APIRouter()

@phone_route.post("/")
def create_phone (phone:Phone = Body(...)):
    try:
        return phone
    except Exception as e:
        print(e)
        return {"error":str(e)}

@phone_route.get("/{id}")
def guardar():
    return {"mensaje": "Guardado con éxito"}

@phone_route.get("/{id}")
def get_phone_by_id(id: int):
    return {"id": id}

@phone_route.put("/{id}")
def update_phone(id: int,phone:Phone = Body(...)):
    return {"id": id, "phone": phone}
