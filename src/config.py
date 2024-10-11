import os
from dataclasses import dataclass
from enum import Enum

from dotenv import load_dotenv

load_dotenv()
load_dotenv(".env.prod", override=True, verbose=True)

class Envs(Enum):
    PROD = 1
    DEV = 2
    TEST = 3


@dataclass
class Config:
    WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
    TELEGRAM_TOKEN = None
    WEATHER_API_KEY = None
    OPENAI_API_KEY = None
    MONGO_URI = None
    PROXY_URL = None
    SENTRY = None
    ENV = Envs.DEV

    def __init__(self):
        self.TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
        self.WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.SENTRY = os.getenv("SENTRY")
