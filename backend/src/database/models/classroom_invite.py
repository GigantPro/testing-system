from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, DateTime, Boolean

from .user import User
from .classroom import Classroom
from ..base import Base


__all__ = ("ClassInvite",)

class ClassInvite(Base):
    __tablename__ = 'classinvite'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    invite_code = Column(String, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    class_id = Column(Integer, ForeignKey(Classroom.id), nullable=False)
    works_end = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    creator_id = Column(Integer, ForeignKey(User.id), nullable=False)
    invites_last = Column(Integer, default=1000000, nullable=False)
