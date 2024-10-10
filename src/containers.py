import logging

from dependency_injector import containers, providers

from src.config import Config
from src.database.database import Database
from src.services.gpt_service import GPTService
from src.services.user_service import UserService
from src.services.weather_service import WeatherService


class Container(containers.DeclarativeContainer):
    config = providers.Singleton(Config)

    # Configure the logger format and level
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
    weather_service = providers.Factory(
        WeatherService,
        config=config,
        logger=logger
    )
    gpt_service = providers.Singleton(
        GPTService,
        config=config,
        logger=logger,
        weather_service=weather_service,
        user_service=user_service
    )
