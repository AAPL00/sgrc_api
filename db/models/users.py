from pydantic import BaseModel

class User(BaseModel):
    name: str
    password: str
    email: str
    phone_number: str
    type: int #0-admin, 1-user

class User_Response(BaseModel):
    name: str
    email: str
    phone_number: str
    type: int #0-admin, 1-user
