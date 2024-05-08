from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .Base import Base
from .BusinessMessage import BusinessMessage


class UploadFiles(Base):
    __tablename__ = "upload_files"

    id: Mapped[int] = mapped_column(primary_key=True)
    business_message_id = mapped_column(ForeignKey("business_messages.id"))
    file_id: Mapped[str] = mapped_column()
