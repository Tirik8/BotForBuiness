from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import os

from app.handlers import mainHandler, businessHandler
from app.database.models import async_main

async def main():
    await async_main()
    
    bot = Bot(token=os.environ.get('BOT_API_KEY')) 
    
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(mainHandler.router, businessHandler.router) 
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())