from telegram import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from src.models.weather_response import WeatherResponse


class WeatherMiniApp:
    BASE_URL = "https://bot.bassmd0.com/"

    def __init__(self, weather_response: WeatherResponse):
        self.weather_response = weather_response

    def generate_url(self):
        url = (
            f"{self.BASE_URL}"
            f"?city={self.weather_response.city}&country={self.weather_response.country}"
            f"&temp={self.weather_response.temp}&feels_like={self.weather_response.feels_like}"
            f"&humidity={self.weather_response.humidity}&wind_speed={self.weather_response.wind_speed}"
            f"&description={self.weather_response.description}"
        )
        return url

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        mini_app_url = self.generate_url()
        keyboard = [
            [InlineKeyboardButton("Abrir Mini App", web_app=WebAppInfo(url=mini_app_url))]
        ]
        return InlineKeyboardMarkup(keyboard)
