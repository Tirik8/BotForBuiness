from aiogram import Router, Bot
from aiogram.types import Message, File, ContentType

router = Router()

@router.business_message(contentent_types=[ContentType.VOICE])
async def handler_voice_message(message: Message):
    voice = message.voice.file_id

    path = "/files/voices"
    #await 