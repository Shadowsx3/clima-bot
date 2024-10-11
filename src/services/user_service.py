import logging

from src.database.database import Database
from src.database.user_db import UserDB


class UserService:
    def __init__(self, database: Database, logger: logging.Logger):
        self.collection = database.get_collection("user_data")
        self.logger = logger

    def get_user(self, user_id: str) -> UserDB:
        self.logger.info(f"Retrieving user {user_id} data")
        return UserDB(user_id, self.collection)
