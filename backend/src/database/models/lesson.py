from datetime import datetime
from sqlalchemy import JSON, TIMESTAMP, Column, Integer, String, func

from ..base import Base


__all__ = ("Lesson",)

class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    type = Column(String)
    title = Column(String, nullable=False)
    description = Column(String)
    tasks_ids = Column(JSON)
    
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    changed_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
