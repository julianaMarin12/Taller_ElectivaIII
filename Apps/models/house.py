from pydantic import BaseModel

class House(BaseModel):
    bathroom: int
    name: str
    price: str
    classification: str
    room: int