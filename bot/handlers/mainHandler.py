from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
import bot.database.requests as rq

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await rq.add_user(message.from_user.id)
    await message.answer(
        f"Привет, {message.from_user.full_name}! Я бот для проверки знаний по Python.\n"
        f"Введи /start для начала теста.\n"
        f"Введи /help для получения справки по командам.",
        reply_markup=ReplyKeyboardRemove()
    )



