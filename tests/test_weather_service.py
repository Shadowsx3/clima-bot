import unittest
from unittest.mock import patch, MagicMock
import logging

import requests

from src.config import Config
from src.models.weather_response import WeatherResponse
from src.services.weather_service import WeatherService


class TestWeatherService(unittest.TestCase):

    def setUp(self):
        self.config = Config()
        self.config.WEATHER_API_KEY = "test_api_key"
        self.config.WEATHER_API_URL = "http://testapiurl.com/weather"

        self.logger = MagicMock(spec=logging.Logger)

        self.weather_service = WeatherService(self.config, self.logger)

    @patch('src.services.weather_service.requests.get')
    def test_get_weather_successful(self, mock_get):
        mock_response = {
            "cod": 200,
            "name": "Salto",
            "sys": {"country": "UY"},
            "main": {
                "temp": 22.0,
                "feels_like": 21.5,
                "humidity": 60
            },
            "wind": {"speed": 5.2},
            "weather": [{"description": "clear sky"}]
        }
        mock_get.return_value.json.return_value = mock_response

        weather = self.weather_service.get_weather("Salto")

        self.assertIsInstance(weather, WeatherResponse)
        self.assertEqual(weather.city, "Salto")
        self.assertEqual(weather.country, "UY")
        self.assertEqual(weather.temp, 22.0)
        self.assertEqual(weather.feels_like, 21.5)
        self.assertEqual(weather.humidity, 60)
        self.assertEqual(weather.wind_speed, 5.2)
        self.assertEqual(weather.description, "clear sky")

        self.logger.info.assert_called_with("Fetching weather for Salto")

    @patch('src.services.weather_service.requests.get')
    def test_get_weather_city_not_found(self, mock_get):
        mock_response = {
            "cod": "404",
            "message": "city not found"
        }
        mock_get.return_value.json.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            self.weather_service.get_weather("UnknownCity")

        self.logger.error.assert_called_with("City not found for request: UnknownCity")
        self.assertEqual(str(context.exception), "City not found")

    @patch('src.services.weather_service.requests.get')
    def test_get_weather_invalid_api_response(self, mock_get):
        mock_response = {
            "cod": 200,
            "name": "Salto",

        }
        mock_get.return_value.json.return_value = mock_response

        with self.assertRaises(KeyError):
            self.weather_service.get_weather("Salto")

        self.logger.info.assert_called_with("Fetching weather for Salto")

    @patch('src.services.weather_service.requests.get')
    def test_get_weather_api_failure(self, mock_get):
        mock_get.side_effect = requests.RequestException("API request failed")

        with self.assertRaises(requests.RequestException):
            self.weather_service.get_weather("Salto")

        self.logger.info.assert_called_with("Fetching weather for Salto")


if __name__ == '__main__':
    unittest.main()
