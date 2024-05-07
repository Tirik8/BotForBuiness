from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .Base import Base
from .BusinessMessage import BusinessMessage

class UploadFiles(Base):
    __tablename__ ='uplead_files'

    id: Mapped[int] = mapped_column(primary_key=True)
    message_id: Mapped[BusinessMessage] = relationship(BusinessMessage.id)
    file_idL: Mapped[str] = mapped_column()