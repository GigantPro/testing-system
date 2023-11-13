from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, JSON

from .user import User
from ..base import Base


__all__ = ("Classroom",)

class Classroom(Base):
    __tablename__ = 'classrooms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey(User.id))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    admins = Column(JSON, nullable=False)
    members = Column(JSON, nullable=False)
    optins = Column(JSON, default=[])
