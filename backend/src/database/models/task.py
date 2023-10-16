from sqlalchemy import JSON, Column, Integer, String

from ..base import Base


__all__ = ("Task",)

class Task(Base):
    __tablename__ = 'Task'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    type = Column(String)
    title = Column(String)
    description = Column(String)
    task = Column(JSON)
    answer = Column(JSON)
