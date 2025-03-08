from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection
from .schemas import UserCreate, UserUpdate

async def create_user(collection: AsyncIOMotorCollection, user: UserCreate):
    new_user = await collection.insert_one(user.dict())
    return str(new_user.inserted_id)

async def get_users(collection: AsyncIOMotorCollection):
    users = await collection.find().to_list(100)
    return [{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]

async def get_user(collection: AsyncIOMotorCollection, user_id: str):
    user = await collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return {"id": str(user["_id"]), "name": user["name"], "email": user["email"]}
    return None

async def update_user(collection: AsyncIOMotorCollection, user_id: str, user: UserUpdate):
    update_data = {k: v for k, v in user.dict().items() if v is not None}
    if update_data:
        await collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    return await get_user(collection, user_id)

async def delete_user(collection: AsyncIOMotorCollection, user_id: str):
    result = await collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0
