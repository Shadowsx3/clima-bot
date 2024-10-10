import json
import logging

from openai import OpenAI

from src.config import Config
from src.services.user_service import UserService
from src.services.weather_service import WeatherService


class GPTService:
    def __init__(self, config: Config, logger: logging.Logger, weather_service: WeatherService,
                 user_service: UserService):
        self.logger = logger
        self.weather_service = weather_service
        self.user_service = user_service
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)

    def process_message_for_detailed_weather(self, message: str, user_id: str) -> str:
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
                    weather_data = self.weather_service.get_weather(location)
                    weather_description = str(weather_data)
                    return weather_description
                else:
                    self.logger.warning(f"Unexpected function call name: {function_call_data.name}")

        except Exception as e:
            self.logger.error(f"Error in GPTService.process_message_for_detailed_weather: {e}")
            return "Lo siento, no pude recuperar la información meteorológica en este momento."
