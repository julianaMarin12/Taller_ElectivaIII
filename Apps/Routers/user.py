from fastapi import APIRouter, Body
from models.user import User

user_route = APIRouter()


@user_route.post("/")
def create_user (user:User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error":str(e)}

@user_route.get("/{id}")
def guardar():
    return {"mensaje": "Guardado con éxito"}

@user_route.get("/{id}")
def get_user_by_id(id: int):
    return {"id": id}

@user_route.put("/{id}")
def update_user(id: int,user:User = Body(...)):
    return {"id": id, "user": user}

@user_route.delete("/{id}")
def delete_user(id: int):
    return {"id": id}