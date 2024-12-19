from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str
    email: str
    phone_number: str
    type: int #0-admin, 1-user