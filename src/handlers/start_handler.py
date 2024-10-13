import logging

from dependency_injector.wiring import Provide
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram import Update
from telegram.ext import CallbackContext

from src.utils.constants import QUIERO_CLIMA, QUIERO_CUENTA
from src.containers import Container
from src.decorators.count_decorator import increase_message_count


@increase_message_count
async def start(update: Update, _context: CallbackContext,
                logger: logging.Logger = Provide[Container.logger]) -> None:
    user_id = str(update.message.from_user.id)
    logger.info(f"Call to start from {user_id}")
    reply_keyboard = [
        [KeyboardButton(QUIERO_CLIMA), KeyboardButton(QUIERO_CUENTA)]
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(
        "¡Hola! Soy Bass 🦔. ¿Qué te gustaría hacer?",
        reply_markup=markup
    )
