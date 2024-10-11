import logging

from dependency_injector.wiring import inject, Provide
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram import Update
from telegram.ext import CallbackContext

from src.constants import QUIERO_CLIMA, QUIERO_CUENTA
from src.containers import Container
from src.decorators.count_decorator import increase_message_count
from src.services.user_service import UserService


@increase_message_count
@inject
async def start(update: Update, context: CallbackContext,
                user_service: UserService = Provide[Container.user_service],
                logger: logging.Logger = Provide[Container.logger]) -> None:
    reply_keyboard = [
        [KeyboardButton(QUIERO_CLIMA), KeyboardButton(QUIERO_CUENTA)]
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(
        "¡Hola! Soy Bass 🦔. ¿Qué te gustaría hacer?",
        reply_markup=markup
    )
