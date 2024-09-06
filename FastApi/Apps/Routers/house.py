from fastapi import APIRouter, Body
from models.house import House
from database import HouseModel


house_route = APIRouter()

@house_route.post("/")
def create_house(house: House = Body(...)):
    HouseModel.create( name= house.name, price =house.price, classification = house.classification, room = house.room)
    return {"message": "House created successfully"}

@house_route.get("/")
def get_house():
    house = HouseModel.select().where(HouseModel.id_house > 0).dicts()
    return list(house)

@house_route.get("/{house_id}")
def get_house(house_id: int):
    try:
        house = HouseModel.get(HouseModel.id_house == house_id)
        return house
    except HouseModel.DoesNotExist:
        return {"error": "House not found"}