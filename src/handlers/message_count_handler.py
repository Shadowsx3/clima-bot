import logging

from dependency_injector.wiring import inject, Provide
from telegram import Update
from telegram.ext import CallbackContext

from src.containers import Container
from src.decorators.count_decorator import increase_message_count
from src.services.user_service import UserService


@increase_message_count
@inject
async def count_handler(
        update: Update,
        _context: CallbackContext,
        user_service: UserService = Provide[Container.user_service],
        logger: logging.Logger = Provide[Container.logger]
) -> None:
    user_id = str(update.message.from_user.id)

    logger.info(f"User {user_id} requested count")
    user = user_service.get_user(user_id)
    user_count = user.get_count()

    await update.message.reply_text(
        f"El contador es: {user_count}"
    )

@increase_message_count
async def handle_count_anyway(
        _update: Update,
        _context: CallbackContext
) -> None:
    pass