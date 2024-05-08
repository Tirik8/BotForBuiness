from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aioredis import Redis

from os import environ

from bot.handlers.commands import Start
from bot.handlers.business import (
    EditMessage,
    TextMessage,
    DeletMessages,
    VoiceMessage,
    PhotoMessage,
)
from bot.database import async_db_main


async def main():
    await async_db_main()

    bot = Bot(token=environ.get("BOT_API_KEY"))

    redis = Redis()
    dp = Dispatcher(storage=RedisStorage(redis=redis))

    dp.include_routers(
        Start.router,
        TextMessage.router,
        DeletMessages.router,
        EditMessage.router,
        VoiceMessage.router,
        PhotoMessage.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
