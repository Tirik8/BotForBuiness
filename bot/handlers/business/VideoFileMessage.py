from aiogram import Router, Bot, F
from aiogram.types import Message
from config import settings
from bot.utils.logs import log

router = Router()


@router.message(F.video)
async def sticker_message(message: Message):
    log(message)
