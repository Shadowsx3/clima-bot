import sys

import sentry_sdk
from dependency_injector.wiring import inject, Provide
from telegram.ext import MessageHandler, filters, CommandHandler, Application, CallbackQueryHandler
from telegram.request import HTTPXRequest

from src.config import Config
from src.constants import QUIERO_CLIMA, QUIERO_CUENTA
from src.containers import Container, LocalConfigAdapter, ProdConfigAdapter, TestConfigAdapter
from src.handlers.default_handle import default_handle
from src.handlers.message_count_handler import count_handler
from src.handlers.start_handler import start
from src.handlers.weather_handler import get_weather, location_callback


@inject
def main(config: Config = Provide[Container.config]) -> None:
    # Initialize application with persistence

    if config.PROXY_URL:
        httpx_proxy = f"http://{config.PROXY_URL}"
        httpx_kwargs = {"verify": False, "proxies": httpx_proxy}
        requests = HTTPXRequest(httpx_kwargs=httpx_kwargs)
        application = Application.builder() \
            .token(config.TELEGRAM_TOKEN) \
            .request(requests) \
            .build()
    else:
        application = Application.builder().token(config.TELEGRAM_TOKEN).build()

    # Handlers for commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("clima", get_weather))
    application.add_handler(CommandHandler("contar", count_handler))

    # Non-command
    application.add_handler(MessageHandler(filters.Text(QUIERO_CLIMA), get_weather))
    application.add_handler(MessageHandler(filters.Text(QUIERO_CUENTA), count_handler))
    application.add_handler(CallbackQueryHandler(location_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, default_handle))

    application.run_polling()


if __name__ == "__main__":
    # Parse env arg
    if len(sys.argv) > 1:
        environment = sys.argv[1]
    else:
        environment = "dev"

    # Initialize container
    if environment == "prod":
        adapters = ProdConfigAdapter()
    elif environment == "dev":
        adapters = LocalConfigAdapter()
    else:
        adapters = TestConfigAdapter()
    container = Container(adapters=adapters)
    container.init_resources()
    container.wire(modules=[__name__], packages=["src.decorators", "src.handlers"])
    Container.configure_logger()

    logger = container.logger()
    logger.info("Starting bot... " + environment)

    if environment != "test" and container.config().SENTRY:
        sentry_sdk.init(
            dsn=container.config().SENTRY,
            traces_sample_rate=1.0,
            profiles_sample_rate=1.0,
            environment=environment,
        )

    # Run bot - #1 Best Comment of the YEAR!!!!
    main()
