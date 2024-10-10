import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MONGO_URI = os.getenv("MONGO_URI")
    WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
