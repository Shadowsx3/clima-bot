import unittest
from unittest.mock import patch, MagicMock
import logging

from src.config import Config
from src.services.weather_service import WeatherService


class TestWeatherService(unittest.TestCase):

    def setUp(self):
        self.config = Config()
        self.config.WEATHER_API_KEY = "test_api_key"

        self.logger = MagicMock(spec=logging.Logger)

        self.weather_service = WeatherService(self.config, self.logger)

    @patch('utils.clients.get_httpx_client')
    def test_get_weather_city_not_found(self, mock_get_httpx_client):
        mock_response = {
            "cod": "404",
            "message": "city not found"
        }

        mock_client = MagicMock()
        mock_client.get.return_value.json.return_value = mock_response
        mock_get_httpx_client.return_value = mock_client

        with self.assertRaises(ValueError) as context:
            self.weather_service.get_weather("UnknownCity")

        self.logger.error.assert_called_with("City not found for request: UnknownCity")
        self.assertEqual(str(context.exception), "City not found")

    @patch('utils.clients.get_httpx_client')
    def test_get_weather_api_failure(self, mock_get_httpx_client):
        mock_client = MagicMock()
        mock_client.get.side_effect = Exception("API request failed")
        mock_get_httpx_client.return_value = mock_client

        with self.assertRaises(Exception):
            self.weather_service.get_weather("Salto")

        self.logger.info.assert_called_with("Fetching weather for Salto")


if __name__ == '__main__':
    unittest.main()
