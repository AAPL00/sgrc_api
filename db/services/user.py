from db.client import client_db

def search_user_by_name(name: str):
    return client_db.users.find_one({"name": name}, {"_id": 0, "pasword": 0})