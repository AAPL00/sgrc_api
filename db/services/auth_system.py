from db.client import client_db
from db.models.users import User, User_Response
from passlib.context import CryptContext

cript = CryptContext(schemes=["bcrypt"])

def insert_user(user: User):
    user.password = cript.hash(user.password)
    user_dict = dict(user)
    return client_db.users.insert_one(user_dict)

def search_user_by_name(name: str):
    user_dict = client_db.users.find_one({"name": name}, {"password": 0})
    return User_Response(**user_dict) if user_dict else None