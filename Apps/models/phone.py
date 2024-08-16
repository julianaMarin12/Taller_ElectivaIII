from pydantic import BaseModel

class Phone(BaseModel):
    id: int
    name: str
    brand: str
    price: str
    detail: str