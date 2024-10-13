import os
from dataclasses import dataclass, field
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class Envs(Enum):
    PROD = 1
    DEV = 2
    TEST = 3


@dataclass
class Config:
    WEATHER_API_URL: str = "https://api.openweathermap.org/data/2.5/weather"
    TELEGRAM_TOKEN: str = field(default_factory=lambda: os.getenv("TELEGRAM_TOKEN"))
    WEATHER_API_KEY: str = field(default_factory=lambda: os.getenv("WEATHER_API_KEY"))
    OPENAI_API_KEY: str = field(default_factory=lambda: os.getenv("OPENAI_API_KEY"))
    MONGO_URI: str = field(default_factory=lambda: os.getenv("MONGO_URI"))
    PROXY_URL: str = field(default_factory=lambda: os.getenv("PROXY_URL"))
    SENTRY: str = field(default_factory=lambda: os.getenv("SENTRY"))
    ENV: Envs = Envs.DEV
