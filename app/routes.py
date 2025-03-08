from fastapi import APIRouter, HTTPException
from .database import user_collection
from .schemas import UserCreate, UserResponse, UserUpdate
from .crud import create_user, get_users, get_user, update_user, delete_user

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def create_user_api(user: UserCreate):
    user_id = await create_user(user_collection, user)
    return UserResponse(id=user_id, **user.dict())

@router.get("/users/", response_model=list[UserResponse])
async def get_users_api():
    return await get_users(user_collection)

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user_api(user_id: str):
    user = await get_user(user_collection, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user_api(user_id: str, user: UserUpdate):
    updated_user = await update_user(user_collection, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}")
async def delete_user_api(user_id: str):
    deleted = await delete_user(user_collection, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
