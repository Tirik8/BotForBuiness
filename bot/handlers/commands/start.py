from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from bot.database.requests import add_user

router = Router()

@router.message(Command('start'))
async def handler_command_start(message: Message):
    await add_user(message.from_user.id)
    await message.answer(
        f"Привет, {message.from_user.full_name}! Я бот для проверки знаний по Python.\n"
        f"Введи /start для начала теста.\n"
        f"Введи /help для получения справки по командам.",
        reply_markup=ReplyKeyboardRemove()
    )
