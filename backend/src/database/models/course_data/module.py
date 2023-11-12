from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey
from sqlalchemy.sql import func

from .task import Task
from ...base import Base
from ..course import Course


__all__ = ("Module",)

class Module(Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    course = Column(ForeignKey(Course.id))
    changed_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    created_time = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    tasks = Column(list[ForeignKey(Task.id)], default=[])
