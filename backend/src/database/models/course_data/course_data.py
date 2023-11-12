from sqlalchemy import TIMESTAMP, Column, Integer, ForeignKey
from sqlalchemy.sql import func

from ...base import Base
from ..course import Course


__all__ = ("CourseData",)

class CourseData(Base):
    __tablename__ = 'courses_data'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    course = Column(ForeignKey(Course.id))
    last_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
