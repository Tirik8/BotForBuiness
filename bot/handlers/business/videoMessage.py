from aiogram import Router, Bot, F
from aiogram.types import Message
from config import settings
from bot.database.requests import add_business_message

router = Router()


@router.message(F.video_note)
async def sticker_message(message: Message):
    pass
