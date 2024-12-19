from db.client import client_db

def auth_validaion(name: str, password: str):
    db_user = client_db.users.find_one({"name": name, "password": password}, {"_id": 0})

def access_token(name: str):
    return {"access_token": name, "token_type": "bearer"}