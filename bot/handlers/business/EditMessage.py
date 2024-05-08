from aiogram import Router, Bot
from aiogram.types import Message
from bot.database.requests import add_business_message

router = Router()


@router.edited_business_message()
async def edit_message(message: Message, bot: Bot):
    business_connection = await bot.get_business_connection(
        message.business_connection_id
    )
    bm = {
        "from_user_id": message.from_user.id,
        "message_id": message.message_id,
        "chat_id": message.chat.id,
        "business_user_id": business_connection.user.id,
        "text": message.text,
        "time": message.date,
    }

    await add_business_message(bm)

    # TODO set new iteration in database( get last iteration from db and write last+1)
