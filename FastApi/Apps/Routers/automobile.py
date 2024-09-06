from fastapi import APIRouter, Body
from models.automobile import Automobile
from database import AutomobileModel


automobile_route = APIRouter()

@automobile_route.post("/")
def create_automobile(automobile: Automobile = Body(...)):
    AutomobileModel.create(name= automobile.name, price =automobile.price, detail = automobile.detail)
    return {"message": "Food created successfully"}

@automobile_route.get("/")
def get_automobile():
    automobile = AutomobileModel.select().where(AutomobileModel.id_house > 0).dicts()
    return list(automobile)

@automobile_route.get("/{automobile_id}")
def get_automobile(automobile_id: int):
    try:
        automobile = AutomobileModel.get(AutomobileModel.id_automobile == automobile_id)
        return automobile
    except AutomobileModel.DoesNotExist:
        return {"error": "Food not found"}