from aiogram import Router, Bot, F
from aiogram.types import Message
from config import settings
from bot.database.requests import add_business_voice

router = Router()


@router.business_message(F.voice)
async def handler_voice_message(message: Message, bot: Bot):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    filename = file_id + ".wav"
    await bot.download_file(
        file_path=file_path, destination=settings.VOICE_PATH + filename
    )
    business_connection = await bot.get_business_connection(
        message.business_connection_id
    )
    business_message_answer = {
        "from_user_id": message.from_user.id,
        "message_id": message.message_id,
        "chat_id": message.chat.id,
        "business_user_id": business_connection.user.id,
        "time": message.date,
        "content_type": "voice",
    }

    await add_business_voice(business_message_answer, filename)
