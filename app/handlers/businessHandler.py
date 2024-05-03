from aiogram import Router, Bot
from aiogram.types import Message, business_messages_deleted, BusinessConnection
from app.database.dataBase import DataBase
from app.database.requests import add_business_message

import re

router = Router()
db = DataBase()

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

    #db.newMessage({"id": message.message_id, "date": message.date, "user_id": message.from_user.id, "text":message.text})

    if message.from_user.id != business_connection.user.id:
        if message.text =='сак' or message.text == 'Сак':
            await message.answer("Сам сак")
        elif re.fullmatch("•*", message.text):
            await message.answer(message.text)
        elif re.fullmatch("[М, м][Д, д][Э, э, А, а, Е, е]*", message.text):
            await message.answer(message.text)

@router.deleted_business_messages()
async def bmsgdel(message: business_messages_deleted, bot: Bot):
    db.deleteMessage(message.chat.id, message.message_ids)
    print(db.selectMessages(message.chat.id, message.message_ids[0]))

    await bot.send_message(business_connection_id = message.business_connection_id, 
                           text = "Зачем удалять сообщения? -_-", chat_id = message.chat.id)
    