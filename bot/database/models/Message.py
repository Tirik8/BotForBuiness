from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .Base import Base

class Message(Base):
    __tablename__ ='messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    from_user_id = mapped_column(ForeignKey('users.id'))
    text: Mapped[str] = mapped_column()
    time: Mapped[str] = mapped_column()
