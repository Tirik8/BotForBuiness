import asyncio

from bot.utils.env import load_env
from bot.utils.logs import start_logging
from bot.main import main

if __name__ == "__main__":

    load_env()

    start_logging()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
