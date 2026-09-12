import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String,Text,DateTime
class Base(DeclarativeBase) :
    pass

class EmailTemplate(Base) :
    __tablename__ = "email_templates"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    template_key: Mapped[str] = mapped_column(String(500), nullable=False)
    name: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    subject_template: Mapped[str] = mapped_column(Text, nullable=False)
    body_html: Mapped[str] = mapped_column(Text, nullable=False)
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_at:Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable= True) 