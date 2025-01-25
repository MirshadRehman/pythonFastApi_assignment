from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGODB_URI= os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DATABASE_NAME= os.getenv("DATABASE_NAME", "bookmanagementsystem")

client= AsyncIOMotorClient(MONGODB_URI)
db= client[DATABASE_NAME]