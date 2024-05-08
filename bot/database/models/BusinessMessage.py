from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .Base import Base


class BusinessMessage(Base):
    __tablename__ = "business_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    from_user_id = mapped_column(BigInteger)
    message_id = mapped_column(BigInteger)
    chat_id = mapped_column(BigInteger)
    business_user_id = mapped_column(BigInteger)
    text: Mapped[str] = mapped_column(nullable=True)
    #filename: Mapped[str] = mapped_column(nullable=True)
    time: Mapped[str] = mapped_column()
    is_deleted: Mapped[bool] = mapped_column(default=False)
    content_type: Mapped[str] = mapped_column(nullable=True)
    files = relationship('upload_files', backref='business_messages')
