from aiogram import Router, Bot
from aiogram.types import business_messages_deleted
from bot.database.requests import get_ans_set_delete_business_messages

router = Router()

@router.deleted_business_messages()
async def handler_business_messages_deleted(message: business_messages_deleted, bot: Bot):
    try:

        messages = await get_ans_set_delete_business_messages(message.chat.id, message.message_ids)

        business_connection = await bot.get_business_connection(message.business_connection_id)

        text = "В чате с пользователем @"+ message.chat.username + " удалены следующие сообщения:\n"
        for message in messages:
            text+= message.text + "\n"

        await bot.send_message(text = text, chat_id = business_connection.user.id)

    except:
        pass
