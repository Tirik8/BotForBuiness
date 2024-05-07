from aiogram import Router, Bot, F
from aiogram.types import Message
from bot.database.requests import add_business_message
from config import settings

router = Router()


@router.business_message(F.photo)
async def handler_business_Photo(message: Message, bot: Bot):
    business_connection = await bot.get_business_connection(
        message.business_connection_id
    )
    print(list(message.photo))
    for photo in list(message.photo):
        file_id = photo.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        filename = file_id + ".jpg"
        await bot.download_file(
            file_path=file_path, destination=settings.PHOTO_PATH + filename
        )

        business_message_answer = {
            "from_user_id": message.from_user.id,
            "message_id": message.message_id,
            "chat_id": message.chat.id,
            "business_user_id": business_connection.user.id,
            "time": message.date,
            "content_type": "photo",
            "filename": filename,
        }

        await add_business_message(business_message_answer)
