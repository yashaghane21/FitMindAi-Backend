import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from motor.motor_asyncio import AsyncIOMotorClient

# Load env variables from .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "fitmind")

class Database:
    client: AsyncIOMotorClient = None
    db = None

db_instance = Database()

def get_database():

    if db_instance.db is None:
        raise RuntimeError("Database not initialized. Please call init_db on application startup.")
    return db_instance.db

async def init_db():
    db_instance.client = AsyncIOMotorClient(MONGO_URI)
    db_instance.db = db_instance.client[MONGO_DB_NAME]
    print(f"Connected to MongoDB: {MONGO_URI} [DB: {MONGO_DB_NAME}]")

async def close_db():
    if db_instance.client:
        db_instance.client.close()
        print("MongoDB connection closed.")
