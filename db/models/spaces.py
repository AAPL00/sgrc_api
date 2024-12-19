from pydantic import BaseModel

class Space(BaseModel):
    name: str
    type: str
    capacity: int
    description: str
    disponibility: bool