import uuid
from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey, UniqueConstraint, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import TimestampMixin

class Job(Base, TimestampMixin):
    __tablename__ = "jobs"
    # __table_args__ = (
    #     UniqueConstraint("external_id", "source_id"),
    # )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # external_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    # source_id: Mapped[uuid.UUID | None] = mapped_column(
    #     UUID(as_uuid=True),
    #     ForeignKey("job_sources.id"),
    #     nullable=True
    # )

    title: Mapped[str] = mapped_column(String(255))
    company: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    location: Mapped[str | None] = mapped_column(String(255))
    salary: Mapped[int | None] = mapped_column(Integer)
    url: Mapped[str] = mapped_column(String(500))