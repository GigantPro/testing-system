from sqlalchemy import JSON, TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.sql import func

from ...base import Base
from .task import Task

__all__ = ("Module",)

class Module(Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    changed_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    created_time = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    tasks = Column(JSON[ForeignKey(Task.id)], default=[])
    course_id = Column(Integer, ForeignKey('courses.id'))
    course_data_id = Column(Integer, ForeignKey('courses_data.id'))
