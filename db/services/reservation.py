from db.client import client_db

def search_reservations_by_user(user_name: str):
    return list(client_db.reservations.find({"reserving_user": user_name}, {"_id": 0}))

