__all__ = (
    "async_session",
    "async_db_main",
)

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import settings
from .models import Base

engine = create_async_engine(settings.DATABASE_URI)
async_session = async_sessionmaker(engine)

async def async_db_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)