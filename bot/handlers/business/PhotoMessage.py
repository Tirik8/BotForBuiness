from aiogram import Router, Bot, F
from aiogram.types import Message
from bot.database.requests import add_business_photos
from config import settings

# from bot.utils.logs import log

router = Router()


@router.business_message(F.photo)
async def handler_business_Photo(message: Message, bot: Bot):
    # log(message)
    business_connection = await bot.get_business_connection(
        message.business_connection_id
    )
    filenames = list()
    # INFO: Вместо message.text в медаиобъектах используется message.caption
    for photo_id in range(0, len(message.photo)):
        photo = message.photo[photo_id]
        file_id = photo.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        filename = file_id + ".jpg"
        filenames.append(filename)
        await bot.download_file(
            file_path=file_path, destination=settings.PHOTO_PATH + filename
        )

    business_message_answer = {
        "from_user_id": message.from_user.id,
        "message_id": message.message_id,
        "chat_id": message.chat.id,
        "business_user_id": business_connection.user.id,
        "time": message.date,
        "text": message.caption,
        "content_type": "photo",
    }

    await add_business_photos(business_message_answer, filenames)
