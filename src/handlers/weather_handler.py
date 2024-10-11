import logging

from dependency_injector.wiring import inject, Provide
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext

from src.containers import Container
from src.decorators.count_decorator import increase_message_count
from src.services.user_service import UserService
from src.services.weather_service import WeatherService
from src.utils.weather_mini_app import WeatherMiniApp


@increase_message_count
@inject
async def get_weather(
        update: Update,
        context: CallbackContext,
        user_service: UserService = Provide[Container.user_service],
        logger: logging.Logger = Provide[Container.logger],
) -> None:
    user_id = str(update.message.from_user.id)
    user = user_service.get_user(user_id)

    last_location = user.get_last_location()
    logger.info(f"User {user_id} requested weather. Last location: {last_location}")
    if last_location:
        keyboard = [
            [
                InlineKeyboardButton("Sí", callback_data="yes"),
                InlineKeyboardButton("No", callback_data="no")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            f"¿Te gustaría usar la última ubicación -> '{last_location}'?",
            reply_markup=reply_markup
        )
        context.user_data["last_location"] = last_location
    else:
        await update.message.reply_text("¿Para qué lugar quisieras saber el clima?")
        context.user_data["awaiting_location"] = True


async def location_callback(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        weather_service: WeatherService = Provide[Container.weather_service],
        logger: logging.Logger = Provide[Container.logger],
) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "yes":
        last_location = context.user_data["last_location"]
        try:
            weather_data = weather_service.get_weather(last_location)
            mini_app = WeatherMiniApp(weather_data)
            await query.edit_message_text(str(weather_data), reply_markup=mini_app.get_reply_markup())
        except Exception as e:
            logger.error(f"Error fetching weather data for {last_location}: {e}")
            await query.edit_message_text("Lo siento, no pude obtener el clima para esa ubicación.")

    elif query.data == "no":
        await query.edit_message_text("¿Para qué lugar quisieras saber el clima?")
        context.user_data["awaiting_location"] = True
