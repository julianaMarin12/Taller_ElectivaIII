from pydantic import BaseModel

class House(BaseModel):
    id: int
    name: str
    price: str
    classification: str
    room: str