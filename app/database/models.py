from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3")

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

class BusinessMessage(Base):
    __tablename__ ='business_messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    from_user_id = mapped_column(ForeignKey('users.id'))
    message_id = mapped_column(BigInteger)
    chat_id = mapped_column(BigInteger)
    business_user_id = mapped_column(BigInteger)
    text: Mapped[str] = mapped_column()
    time: Mapped[str] = mapped_column()
    is_deleted: Mapped[bool] = mapped_column(default=False)

class Message(Base):
    __tablename__ ='messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    from_user_id = mapped_column(ForeignKey('users.id'))
    text: Mapped[str] = mapped_column()
    time: Mapped[str] = mapped_column()

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
