import unittest
from unittest.mock import MagicMock, patch
import logging

from src.database.database import Database
from src.services.user_service import UserService


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.mock_database = MagicMock(spec=Database)
        self.mock_logger = MagicMock(spec=logging.Logger)

        self.mock_collection = MagicMock()
        self.mock_database.get_collection.return_value = self.mock_collection

        self.user_service = UserService(self.mock_database, self.mock_logger)

    def test_get_user_initializes_userdb(self):
        user_id = "12345"

        with patch('src.services.user_service.UserService.get_user') as MockUserDB:
            user = self.user_service.get_user(user_id)

            MockUserDB.assert_called_once_with(user_id)

            self.assertEqual(user, MockUserDB.return_value)

            self.mock_database.get_collection.assert_called_once_with("user_data")


if __name__ == '__main__':
    unittest.main()
