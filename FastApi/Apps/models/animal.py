from pydantic import BaseModel

class Animal(BaseModel):
    id: int
    name: str
    gender: str
    classification: str
    age: int
    owner: str
