from dependency_injector.wiring import inject, Provide
from telegram.ext import MessageHandler, filters, CommandHandler, PicklePersistence, Application, CallbackQueryHandler

from src.config import Config
from src.constants import QUIERO_CLIMA, QUIERO_CUENTA
from src.containers import Container
from src.handlers.message_count_handler import count_handler, handle_count_anyway
from src.handlers.start_handler import start
from src.handlers.weather_handler import get_weather, location_callback, handle_new_location


@inject
def main(config: Config = Provide[Container.config]) -> None:
    # Initialize application with persistence
    persistence = PicklePersistence(filepath="weatherbot")
    application = Application.builder().token(config.TELEGRAM_TOKEN).persistence(persistence).build()

    # Handlers for commands
    application.add_handler(CommandHandler("start", start))

    # Weather
    application.add_handler(CommandHandler("clima", get_weather))
    application.add_handler(MessageHandler(filters.Text(QUIERO_CLIMA), get_weather))
    application.add_handler(CallbackQueryHandler(location_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_new_location))

    # Count
    application.add_handler(CommandHandler("contar", count_handler))
    application.add_handler(MessageHandler(filters.Text(QUIERO_CUENTA), count_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_count_anyway))

    application.run_polling()

if __name__ == "__main__":
    # Initialize container
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    Container.configure_logger()

    logger = container.logger()
    logger.info("Starting bot...")

    # Run bot
    main()
