from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, Boolean, FLOAT

from ..base import Base


__all__ = ("Course",)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    ico_url = Column(String, default='/api/static/standart_ico.png', nullable=False)
    teachers_ids = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    passing_id = Column(JSON[int], default=[])
    passed_id = Column(JSON, default=[])
    reviews = Column(JSON, default=[])
    rating = Column(FLOAT, default=.0)
    course_data = Column(JSON, default={})
