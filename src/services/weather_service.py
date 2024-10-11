import logging

from src.config import Config
from src.models.weather_response import WeatherResponse
from utils.clients import get_httpx_client


class WeatherService:
    def __init__(self, config: Config, logger: logging.Logger):
        self.api_key = config.WEATHER_API_KEY
        self.api_url = config.WEATHER_API_URL
        self.logger = logger

    def get_weather(self, location: str) -> WeatherResponse:
        self.logger.info(f"Fetching weather for {location}")
        params = {
            "q": location,
            "appid": self.api_key,
            "units": "metric",
            "lang": "es"
        }

        response = get_httpx_client().get(self.api_url, params=params).json()

        if response.get("cod") != 200:
            self.logger.error(f"City not found for request: {location}")
            raise ValueError("City not found")

        city = response["name"]
        country = response["sys"]["country"]
        temp = response["main"]["temp"]
        feels_like = response["main"]["feels_like"]
        humidity = response["main"]["humidity"]
        wind_speed = response["wind"]["speed"]
        description = response["weather"][0]["description"]

        return WeatherResponse(city, country, temp, feels_like, humidity, wind_speed, description)
