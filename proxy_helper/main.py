import asyncio
import threading

from console.cli_console import CLIConsole
from proxy.proxy_runner import start_proxy


def start_cli():
    console = CLIConsole()
    console.cmdloop()


def start_proxy_async():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_proxy())


if __name__ == "__main__":
    proxy_thread = threading.Thread(target=start_proxy_async)
    proxy_thread.daemon = True
    proxy_thread.start()

    start_cli()
