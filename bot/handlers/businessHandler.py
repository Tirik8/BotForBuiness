from aiogram import Router, Bot
from aiogram.types import Message, business_messages_deleted, BusinessConnection
from bot.database.requests import add_business_message, get_business_messages

import re

router = Router()

@router.business_message()
async def bmsg(message: Message, bot: Bot):
    business_connection = await bot.get_business_connection(message.business_connection_id)
    bm = {
        "from_user_id": message.from_user.id,
        "message_id": message.message_id,
        "chat_id": message.chat.id,
        "business_user_id": business_connection.user.id,
        "text": message.text,
        "time": message.date,
    }
    
    await add_business_message(bm)

    if message.from_user.id != business_connection.user.id:
        if message.text =='сак' or message.text == 'Сак':
            await message.answer("Сам сак")
        elif re.fullmatch("•*", message.text):
            await message.answer(message.text)
        elif re.fullmatch("[М, м][Д, д][Э, э, А, а, Е, е]*", message.text):
            await message.answer(message.text)


@router.deleted_business_messages()
async def bmsgdel(message: business_messages_deleted, bot: Bot):
    try:
        messages = await get_business_messages(message.chat.id, message.message_ids)
        business_connection = await bot.get_business_connection(message.business_connection_id)

        text = "В чате с пользователем @"+ message.chat.username + " удалены следующие сообщения:\n"
        for message in messages:
            text+= message.text + "\n"

        await bot.send_message(text = text, chat_id = business_connection.user.id)

    except:
        pass

    