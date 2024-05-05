from bot.database import async_session
from bot.database.models import User

from sqlalchemy import select, insert

async def add_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user is None:
            await session.execute(insert(User).values(tg_id=tg_id))
            await session.commit()