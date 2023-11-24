from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from config import MONGO_DB_URI

mongo = MongoClient(MONGO_DB_URI)

db = mongo.bunny
