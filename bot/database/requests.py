from bot.database.models import async_session
from bot.database.models import User, Message, BusinessMessage

from sqlalchemy import select, update, delete, insert

async def add_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user is None:
            await session.execute(insert(User).values(tg_id=tg_id))
            await session.commit()
                                
async def add_business_message(business_message: dict) -> None:
    async with async_session() as session:
        await session.execute(insert(BusinessMessage).values(**business_message))
        await session.commit()

async def get_business_messages(chat_id: int, ids: list) -> list:
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
