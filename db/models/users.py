from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    password: str
    email: EmailStr
    phone_number: str
    level: int #0-admin, 1-user

class User_Response(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    level: int #0-admin, 1-user