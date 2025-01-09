from fastapi import APIRouter, HTTPException, status
from db.models.spaces import Space
from db.services.spaces import search_space_by_name, insert_space, delete_space_by_name

space_router = APIRouter()

@space_router.post("/space", response_model=Space, status_code=status.HTTP_201_CREATED)
async def create_new_space(space: Space):
    if not search_space_by_name(space.name):
        insert_space(space)
        return space
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Space name already in database")
    
@space_router.get("/space/{name}", response_model=Space, status_code=status.HTTP_200_OK)
async def get_space(name: str):
    space = search_space_by_name(name)
    if not space:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Space not found")
    else:
        return space
    
@space_router.delete("/space/{name}", status_code=status.HTTP_204_NO_CONTENT):
async def delete_space(name: str):
    if not delete_space_by_name(name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Space not found")
    else:
        return "Deleted"
    
#@space_router.put("/space/", response_model=Space, status_code=status.HTTP_202_ACCEPTED)
#async def update_space(space: Space):
    