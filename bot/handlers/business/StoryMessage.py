from aiogram import Router, Bot, F
from aiogram.types import Message
from bot.utils.logs import log

router = Router()


@router.message(F.story)
async def sticker_message(message: Message):
    log(message)
