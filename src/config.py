import os
from dataclasses import dataclass
from enum import Enum

from dotenv import load_dotenv

load_dotenv()

class Envs(Enum):
    PROD = 1
    DEV = 2
    TEST = 3

@dataclass
class Config:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MONGO_URI = os.getenv("MONGO_URI")
    WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
    ENV = Envs.DEV

