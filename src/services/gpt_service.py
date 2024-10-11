import json
import logging

from openai import OpenAI

from src.models.weather_response import WeatherResponse
from src.services.user_service import UserService
from src.services.weather_service import WeatherService


class GPTService:
    def __init__(self, logger: logging.Logger, weather_service: WeatherService,
                 user_service: UserService, openai_client: OpenAI):
        self.logger = logger
        self.weather_service = weather_service
        self.user_service = user_service
        self.client = openai_client

    def process_message_for_detailed_weather(self, message: str, user_id: str) -> WeatherResponse:
        function = {
            "name": "get_weather_for_city",
            "description": "Fetches detailed weather information based on city name and country code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "'City name,Country Code' for which to get detailed weather information."
                    }
                },
                "required": ["location"]
            }
        }
        try:
            response = self.client.chat.completions.create(model="gpt-3.5-turbo",
                                                           messages=[
                                                               {"role": "user", "content": f"Clima de: {message}"}],
                                                           functions=[function],
                                                           function_call="auto")
            self.logger.info(response.choices[0].message.function_call)
            if response.choices[0].message.function_call:
                function_call_data = response.choices[0].message.function_call
                if function_call_data.name == "get_weather_for_city":
                    arguments = json.loads(function_call_data.arguments)
                    location = arguments['location']
                    self.logger.info(f"Calling OpenWeather with {location} and saving it")
                    user = self.user_service.get_user(user_id)
                    if user:
                        user.save_last_location(location)
                    return self.weather_service.get_weather(location)
                else:
                    self.logger.warning(f"Unexpected function call")

        except Exception as e:
            self.logger.error(f"Error in GPTService.process_message_for_detailed_weather: {e}")
            raise e
