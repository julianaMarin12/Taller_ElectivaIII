from pydantic import BaseModel

class Automobile(BaseModel):
    id: int
    name: str
    price: float
    classification: str
    weight: float