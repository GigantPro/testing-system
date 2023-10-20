from sqlalchemy import JSON, Column, Integer, String

from ..base import Base


__all__ = ("Lesson",)

class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    type = Column(String)
    title = Column(String, nullable=False)
    description = Column(String)
    tasks_ids = Column(JSON)
