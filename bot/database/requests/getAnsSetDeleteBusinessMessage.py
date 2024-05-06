from bot.database import async_session
from bot.database.models import BusinessMessage

from sqlalchemy import select, update

async def get_ans_set_delete_business_messages(chat_id: int, ids: list) -> list:
    async with async_session() as session:
        result = await session.execute(update(BusinessMessage)
                                .where(BusinessMessage.chat_id == chat_id)
                                .filter(BusinessMessage.message_id.in_(ids))
                                .values(is_deleted=True)
                                )
        await session.commit()
    
    async with async_session() as session:
        result = await session.execute(select(BusinessMessage)
                                       .where(BusinessMessage.chat_id == chat_id)
                                       .filter(BusinessMessage.message_id.in_(ids))
                                       )
        return result.scalars().all()