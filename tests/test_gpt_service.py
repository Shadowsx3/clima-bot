import unittest
from unittest.mock import MagicMock
import logging
import json

from src.services.user_service import UserService
from src.services.weather_service import WeatherService
from src.services.gpt_service import GPTService


class TestGPTService(unittest.TestCase):

    def setUp(self):
        self.mock_logger = MagicMock(spec=logging.Logger)
        self.mock_weather_service = MagicMock(spec=WeatherService)
        self.mock_user_service = MagicMock(spec=UserService)
        self.mock_openai_client = MagicMock()

        self.gpt_service = GPTService(
            logger=self.mock_logger,
            weather_service=self.mock_weather_service,
            user_service=self.mock_user_service,
            openai_client=self.mock_openai_client
        )

    def test_process_message_for_detailed_weather_success(self):
        mock_function_call_data = {
            "name": "get_weather_for_city",
            "arguments": json.dumps({"location": "Salto,UY"})
        }
        mock_openai_response = MagicMock()
        mock_openai_response.choices = [MagicMock()]
        mock_openai_response.choices[0].message.function_call = MagicMock()
        mock_openai_response.choices[0].message.function_call.name = "get_weather_for_city"
        mock_openai_response.choices[0].message.function_call.arguments = mock_function_call_data['arguments']
        self.mock_openai_client.chat.completions.create.return_value = mock_openai_response

        mock_user = MagicMock()
        self.mock_user_service.get_user.return_value = mock_user
        mock_weather_data = MagicMock()
        mock_weather_data.__str__.return_value = "Soleado, 25°C"
        self.mock_weather_service.get_weather.return_value = mock_weather_data

        result = str(self.gpt_service.process_message_for_detailed_weather("Salto,UY", "12345"))

        self.mock_openai_client.chat.completions.create.assert_called_once()

        self.mock_user_service.get_user.assert_called_once_with("12345")
        mock_user.save_last_location.assert_called_once_with("Salto,UY")
        self.mock_weather_service.get_weather.assert_called_once_with("Salto,UY")

        self.assertEqual(result, "Soleado, 25°C")
        self.mock_logger.info.assert_any_call(f"Calling OpenWeather with Salto,UY and saving it")

    def test_process_message_for_detailed_weather_unexpected_function_call(self):
        mock_openai_response = MagicMock()
        mock_openai_response.choices = [MagicMock()]
        mock_openai_response.choices[0].message.function_call = MagicMock(name="another_function")
        self.mock_openai_client.chat.completions.create.return_value = mock_openai_response

        result = self.gpt_service.process_message_for_detailed_weather("Salto,UY", "12345")

        self.mock_weather_service.get_weather.assert_not_called()
        self.mock_user_service.get_user.assert_not_called()

        self.mock_logger.warning.assert_called_once_with("Unexpected function call")

        self.assertIsNone(result)

    def test_process_message_for_detailed_weather_exception(self):
        self.mock_openai_client.chat.completions.create.side_effect = Exception("OpenAI error")

        with self.assertRaises(Exception):
            self.gpt_service.process_message_for_detailed_weather("Salto,UY", "12345")

        self.mock_logger.error.assert_called_once_with(
            "Error in GPTService.process_message_for_detailed_weather: OpenAI error"
        )


if __name__ == '__main__':
    unittest.main()
