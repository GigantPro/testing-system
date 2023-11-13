from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey, JSON, String
from sqlalchemy.sql import func

from .task import Task
from ...base import Base


__all__ = ("Module",)

class Module(Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    changed_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    created_time = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    tasks = Column(JSON[ForeignKey(Task.id)], default=[])
