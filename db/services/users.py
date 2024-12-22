from db.client import client_db
from db.models.users import User_Response, User
from db.services.auth_system import cript

def insert_user(user: User):
    user.password = cript.hash(user.password)
    user_dict = dict(user)
    return client_db.users.insert_one(user_dict)

def search_user_by_name(name: str):
    user = client_db.users.find_one({"name": name}, {"password": 0})
    return User_Response(**user) if user else None

