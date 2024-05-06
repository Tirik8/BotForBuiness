from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from .Base import Base


class BusinessMessage(Base):
    __tablename__ = "business_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    from_user_id = mapped_column(ForeignKey("users.id"))
    message_id = mapped_column(BigInteger)
    chat_id = mapped_column(BigInteger)
    business_user_id = mapped_column(BigInteger)
    text: Mapped[str] = mapped_column(nullable=True)
    filename: Mapped[str] = mapped_column(nullable=True)
    time: Mapped[str] = mapped_column()
    is_deleted: Mapped[bool] = mapped_column(default=False)
    content_type: Mapped[str] = mapped_column(nullable=True)
