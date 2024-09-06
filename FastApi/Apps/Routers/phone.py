from fastapi import APIRouter, Body
from models.phone import Phone
from database import PhoneModel


phone_route = APIRouter()

@phone_route.post("/")
def create_phone(phone: Phone = Body(...)):
    PhoneModel.create(name= phone.name, brand =phone.brand, price = phone.price, detail = phone.detail)
    return {"message": "Phone created successfully"}

@phone_route.get("/")
def get_phone():
    phone = PhoneModel.select().where(PhoneModel.id_phone > 0).dicts()
    return list(phone)

@phone_route.get("/{phone_id}")
def get_phone(phone_id: int):
    try:
        phone = PhoneModel.get(PhoneModel.id_phone == phone_id)
        return phone
    except PhoneModel.DoesNotExist:
        return {"error": "Phone not found"}