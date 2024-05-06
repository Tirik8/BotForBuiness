from aiogram import Router, Bot
from aiogram.types import Message
from bot.database.requests import add_business_message
from bot.utils.answer import answer

router = Router()


@router.business_message()
async def handler_business_message(message: Message, bot: Bot):
    business_connection = await bot.get_business_connection(
        message.business_connection_id
    )
    business_message = {
        "from_user_id": message.from_user.id,
        "message_id": message.message_id,
        "chat_id": message.chat.id,
        "business_user_id": business_connection.user.id,
        "text": message.text,
        "time": message.date,
    }

    await add_business_message(business_message)

    if message.from_user.id != business_connection.user.id:
        ans = answer(message.text)
        if ans:
            message_answer = await message.answer(ans)

            business_message_answer = {
                "from_user_id": message_answer.from_user.id,
                "message_id": message_answer.message_id,
                "chat_id": message_answer.chat.id,
                "business_user_id": business_connection.user.id,
                "text": message_answer.text,
                "time": message_answer.date,
            }
            await add_business_message(business_message_answer)
