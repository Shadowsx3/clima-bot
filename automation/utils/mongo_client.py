import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

class MongoClient:
    def __init__(self):
        self.client = pymongo.MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client[os.getenv("MONGO_DATABASE")]

    def set_count(self, user_id: str, count: int):
        self.db.user_data.update_one(
            {"user_id": user_id},
            {"$set": {"count": count}},
            upsert=True
        )

    def get_count(self, user_id: str):
        user_data = self.db.user_data.find_one({"user_id": user_id})
        return user_data['count'] if user_data else 0
