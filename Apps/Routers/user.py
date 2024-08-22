from fastapi import APIRouter, Body
from Apps.models.user import User


user_route = APIRouter()

@user_route.post("/")
def create_users (user:User = Body(...)):
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
def update_user(id: int,user:User = Body(...) ):
    return {"id": id, "user": user}

@user_route.delete("/{user_id}")
def delete_user(user_id: int):
    return {"user_id": user_id}
