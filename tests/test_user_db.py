import unittest
from unittest.mock import MagicMock
from pymongo.collection import Collection

from src.database.user_db import UserDB


class TestUserDB(unittest.TestCase):

    def setUp(self):
        self.mock_collection = MagicMock(spec=Collection)

        self.user_id = "12345"
        self.user_db = UserDB(self.user_id, self.mock_collection)

    def test_get_count_existing_user(self):
        self.mock_collection.find_one.return_value = {"user_id": self.user_id, "count": 10}

        count = self.user_db.get_count()
        self.assertEqual(count, 10)

        self.mock_collection.find_one.assert_called_once_with({"user_id": self.user_id})

    def test_get_count_nonexistent_user(self):
        self.mock_collection.find_one.return_value = None

        count = self.user_db.get_count()
        self.assertEqual(count, 0)

        self.mock_collection.find_one.assert_called_once_with({"user_id": self.user_id})

    def test_increment_count(self):
        self.user_db.increment_count()

        self.mock_collection.update_one.assert_called_once_with(
            {"user_id": self.user_id},
            {"$inc": {"count": 1}},
            upsert=True
        )

    def test_save_last_location(self):
        location = "Salto"
        self.user_db.save_last_location(location)

        self.mock_collection.update_one.assert_called_once_with(
            {"user_id": self.user_id},
            {"$set": {"last_location": location}},
            upsert=True
        )

    def test_get_last_location_existing_user(self):
        self.mock_collection.find_one.return_value = {"user_id": self.user_id, "last_location": "Barcelona"}

        location = self.user_db.get_last_location()
        self.assertEqual(location, "Barcelona")

        self.mock_collection.find_one.assert_called_once_with({"user_id": self.user_id})

    def test_get_last_location_nonexistent_user(self):
        self.mock_collection.find_one.return_value = None

        location = self.user_db.get_last_location()
        self.assertIsNone(location)

        self.mock_collection.find_one.assert_called_once_with({"user_id": self.user_id})


if __name__ == '__main__':
    unittest.main()
