import logging
import os

from dependency_injector import containers, providers
from openai import OpenAI

from src.config import Config, Envs
from src.database.database import Database
from src.services.gpt_service import GPTService
from src.services.user_service import UserService
from src.services.weather_service import WeatherService


class Container(containers.DeclarativeContainer):
    adapters = providers.DependenciesContainer()

    config = adapters.config

    @staticmethod
    def configure_logger():
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
        )
        logging.getLogger("httpx").setLevel(logging.WARNING)
        return logging.getLogger(__name__)

    logger = providers.Singleton(configure_logger)

    database = providers.Singleton(Database, config=config)

    user_service = providers.Singleton(UserService, database=database, logger=logger)

    weather_service = providers.Singleton(
        WeatherService,
        config=config,
        logger=logger
    )

    openai_client = providers.Factory(OpenAI, api_key=os.getenv("OPENAI_API_KEY"))
    gpt_service = providers.Factory(
        GPTService,
        logger=logger,
        weather_service=weather_service,
        user_service=user_service,
        openai_client=openai_client
    )


class LocalConfigAdapter(containers.DeclarativeContainer):
    @staticmethod
    def get_config():
        config = Config()
        config.MONGO_URI = os.getenv("MONGO_URI_DEV")
        config.ENV = Envs.DEV
        return config

    config = providers.Singleton(get_config)


class ProdConfigAdapter(containers.DeclarativeContainer):
    @staticmethod
    def get_config():
        config = Config()
        config.MONGO_URI = os.getenv("MONGO_URI")
        config.ENV = Envs.PROD
        return config

    config = providers.Singleton(get_config)
