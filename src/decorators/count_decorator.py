import logging
from functools import wraps

from dependency_injector.wiring import Provide
from sentry_sdk import set_user
from telegram import Update
from telegram.ext import CallbackContext

from src.containers import Container
from src.services.user_service import UserService


def increase_message_count(func):
    @wraps(func)
    async def wrapper(
            update: Update,
            context: CallbackContext,
            *args, **kwargs
    ) -> None:
        user_service, logger = get_dependencies()
        user_id = str(update.message.from_user.id)
        set_user({"user_id": user_id, "username": update.message.from_user.username})

        user_service.get_user(user_id).increment_count()
        logger.info(f"Increasing count for user {user_id}")

        return await func(update, context, *args, **kwargs)

    return wrapper


def get_dependencies(
        user_service: UserService = Provide[Container.user_service],
        logger: logging.Logger = Provide[Container.logger]
):
    return user_service, logger
