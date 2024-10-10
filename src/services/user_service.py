import logging

from src.database.database import Database
from src.models.user import User


class UserService:
    def __init__(self, database: Database, logger: logging.Logger):
        self.collection = database.get_collection("user_data")
        self.logger = logger

    def get_user(self, user_id: str) -> User:
        self.logger.info(f"Retrieving user {user_id} data")
        return User(user_id, self.collection)
