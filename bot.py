import sys

import sentry_sdk
from dependency_injector.wiring import Provide
from telegram.ext import MessageHandler, filters, CommandHandler, Application, CallbackQueryHandler
from telegram.request import HTTPXRequest

from src.config import Config
from src.handlers.default_handler import error_handler, default_handler
from src.utils.constants import QUIERO_CLIMA, QUIERO_CUENTA
from src.containers import Container, LocalConfigAdapter, ProdConfigAdapter, TestConfigAdapter
from src.handlers.message_count_handler import count_handler
from src.handlers.start_handler import start
from src.handlers.weather_handler import get_weather, location_callback


def main(config: Config = Provide[Container.config]) -> None:
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
    application.add_handler(MessageHandler(filters.Regex(f"^{QUIERO_CLIMA}$"), get_weather))
    application.add_handler(MessageHandler(filters.Regex(f"^{QUIERO_CUENTA}$"), count_handler))
    application.add_handler(CallbackQueryHandler(location_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, default_handler))

    # Add error handler
    application.add_error_handler(error_handler)

    application.run_polling()


if __name__ == "__main__":
    # Parse env arg
    if len(sys.argv) > 1:
        environment = sys.argv[1]
    else:
        environment = "dev"

    # Initialize container
    match environment:
        case "prod":
            adapters = ProdConfigAdapter()
        case "dev":
            adapters = LocalConfigAdapter()
        case _:
            adapters = TestConfigAdapter()
    container = Container(adapters=adapters)
    container.init_resources()
    container.wire(modules=[__name__], packages=["src.decorators", "src.handlers"])

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
