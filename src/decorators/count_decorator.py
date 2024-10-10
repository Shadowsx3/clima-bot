import logging
from functools import wraps

from dependency_injector.wiring import inject, Provide
from telegram import Update
from telegram.ext import CallbackContext

from src.containers import Container
from src.services.user_service import UserService


def increase_message_count(func):
    @inject
    @wraps(func)
    async def wrapper(
            update: Update,
            context: CallbackContext,
            user_service: UserService = Provide[Container.user_service],
            logger: logging.Logger = Provide[Container.logger],
            *args, **kwargs
    ) -> None:
        user_id = str(update.message.from_user.id)
        user_service.get_user(user_id).increment_count()
        logger.info(f"Increasing count for user {user_id}")
        return await func(update, context, user_service, logger, *args, **kwargs)

    return wrapper
