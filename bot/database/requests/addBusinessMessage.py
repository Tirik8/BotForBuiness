from bot.database import async_session
from bot.database.models import BusinessMessage

from sqlalchemy import insert


async def add_business_message(business_message: dict) -> None:
    async with async_session() as session:
        await session.execute(insert(BusinessMessage).values(**business_message))
        await session.commit()
