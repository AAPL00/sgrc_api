from pydantic import BaseModel

class Space(BaseModel):
    name: str
    clasification: int #0-meeting hall, 1-private cabinet
    capacity: int
    description: str
    disponibility: bool