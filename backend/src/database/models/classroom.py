from datetime import datetime

from sqlalchemy import JSON, TIMESTAMP, Column, ForeignKey, Integer, String, func

from ..base import Base
from .user import User

__all__ = ("Classroom",)

class Classroom(Base):
    __tablename__ = 'classrooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey(User.id))
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    changed_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    admins = Column(JSON, nullable=False)
    members = Column(JSON, nullable=False)
    optins = Column(JSON, default=[])
