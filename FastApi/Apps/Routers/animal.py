from fastapi import APIRouter, Body
from models.animal import Animal
from database import AnimalModel


animal_route = APIRouter()

@animal_route.post("/")
def create_animal(animal: Animal = Body(...)):
        AnimalModel.create(name= animal.name, id =animal.id, gender = animal.gender, classification = animal.classification, age = animal.age, owner = animal.owner)
        return {"message": "Food created successfully"}

@animal_route.get("/")
def get_animal():
    animal = AnimalModel.select().where(AnimalModel.id_animal > 0).dicts()
    return list(animal)

@animal_route.get("/{animal_id}")
def get_animal(animal_id: int):
    try:
        animal = AnimalModel.get(AnimalModel.id_animal ==  animal_id)
        return animal
    except AnimalModel.DoesNotExist:
        return {"error": "Food not found"}