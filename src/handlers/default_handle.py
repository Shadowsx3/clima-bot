import logging

from dependency_injector.wiring import Provide
from telegram import Update
from telegram.ext import CallbackContext

from src.containers import Container
from src.decorators.count_decorator import increase_message_count
from src.services.gpt_service import GPTService
from src.mini_app.weather_mini_app import WeatherMiniApp


@increase_message_count
async def default_handle(
        update: Update,
        context: CallbackContext,
        logger: logging.Logger = Provide[Container.logger],
        gpt_service: GPTService = Provide[Container.gpt_service],
) -> None:
    if context.user_data.get("awaiting_location", False):
        location_text = update.message.text
        user_id = str(update.message.from_user.id)
        logger.info(f"Handle new location for {user_id}")
        try:
            weather_data = gpt_service.process_message_for_detailed_weather(location_text, user_id)
            mini_app = WeatherMiniApp(weather_data)
            await update.message.reply_text(str(weather_data), reply_markup=mini_app.get_reply_markup())
        except Exception as e:
            logger.error(f"Error processing new location '{location_text}': {e}")
            await update.message.reply_text("Lo siento, no pude procesar la ubicación proporcionada.")
        finally:
            context.user_data["awaiting_location"] = False