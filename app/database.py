from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import quote_plus

username = "admin"
password = "Krishna@2025"  

encoded_password = quote_plus(password)

MONGO_URI = f"mongodb+srv://{username}:{encoded_password}@alphabloczs.eusq9.mongodb.net/?retryWrites=true&w=majority&appName=alphabloczs"

DATABASE_NAME = "fastapi_db"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE_NAME]
user_collection = database["users"]




