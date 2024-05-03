from app.database.models import async_session
from app.database.models import User, Message, BusinessMessage

from sqlalchemy import select, update, delete, insert

async def add_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user is None:
            await session.execute(insert(User).values(tg_id=tg_id))
            await session.commit()
                                