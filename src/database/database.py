from pymongo import MongoClient

from src.config import Config


class Database:
    def __init__(self, config: Config):
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client.get_database()

    def get_collection(self, name):
        return self.db[name]
