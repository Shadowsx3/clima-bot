from pymongo.collection import Collection

class User:
    def __init__(self, user_id: str, collection: Collection):
        self.user_id = user_id
        self.collection = collection

    def get_count(self) -> int:
        result = self.collection.find_one({"user_id": self.user_id})
        return result.get("count", 0) if result else 0

    def increment_count(self):
        self.collection.update_one(
            {"user_id": self.user_id},
            {"$inc": {"count": 1}},
            upsert=True
        )

    def save_last_location(self, location: str):
        self.collection.update_one(
            {"user_id": self.user_id},
            {"$set": {"last_location": location}},
            upsert=True
        )

    def get_last_location(self) -> str:
        result = self.collection.find_one({"user_id": self.user_id})
        return result.get("last_location") if result else None
