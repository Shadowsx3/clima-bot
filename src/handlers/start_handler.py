from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes, CallbackContext

from src.constants import QUIERO_CLIMA, QUIERO_CUENTA
from src.decorators.count_decorator import increase_message_count


@increase_message_count
async def start(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [
        [KeyboardButton(QUIERO_CLIMA), KeyboardButton(QUIERO_CUENTA)]
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "¡Hola! Soy Bass 🦔. ¿Qué te gustaría hacer?",
        reply_markup=markup
    )
