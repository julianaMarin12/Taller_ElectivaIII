from pydantic import BaseModel

class Food(BaseModel):
    id: int
    name: str
    price: str
    detail: str