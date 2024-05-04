import asyncio
from dotenv import load_dotenv

from app.utils.logs import start_logging
from app.main import main

if __name__ == "__main__":

    load_dotenv(".env")

    start_logging()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


# ---OK---- TODO: env vars for bot config 
# ---OK---- TODO: rewrite bot to async
# ---30%--- TODO: database with SQLalchemy ORM (async) [subscribes, price list, messages, users, users configs]?
# ---OK---- TODO: include redis
# ---OK---- TODO: include advanced logging
# TODO: config menu for subscribers with configurate answers (regular expression?)
# TODO: inline buttons (with another library?)
# TODO: telegram payments for subscribe
# TODO: admins for bot? (admins can subscribe, unsubscribe, edit price list, edit config)
# TODO: handlers for voice, video and picture messages
# TODO: fields for resend messages and answers
# TODO: hadnler for rewited messages