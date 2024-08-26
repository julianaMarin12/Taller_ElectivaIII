from pydantic import BaseModel

class Automobile(BaseModel):
    door: int
    name: str
    price: float
    classification: str
    weight: float