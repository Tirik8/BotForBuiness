from aiogram import Router, Bot
from aiogram.types import Message, business_messages_deleted
from app.database.dataBase import DataBase

import re

router = Router()
db = DataBase()

@router.business_message()
async def bmsg(message: Message):
    
    db.newMessage({"id": message.message_id, "date": message.date, "user_id": message.from_user.id, "text":message.text})

    if message.from_user.id != 426776987:

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
    