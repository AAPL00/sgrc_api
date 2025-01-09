from db.client import client_db
from db.models.spaces import Space

def insert_space(space: Space):
    space_dict = dict(space)
    client_db.spaces.insert_one(space_dict)

def search_space_by_name(name: str):
    space = client_db.spaces.find_one({"name": name})
    return Space(**space) if space else None

def delete_space_by_name(name: str):
    return True if client_db.spaces.delete_one({"name": name}).deleted_count else False

def update_space(space: Space):
    space_dict = dict(space)
    space_dict_before = client_db.spaces.find_one_and_replace({"name": space.name}, space_dict)
    space_dict_after = client_db.spaces.find_one({"name": space.name})
    return (space_dict_before, space_dict_after)