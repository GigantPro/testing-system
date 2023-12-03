from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, DateTime, Boolean, func

from .user import User
from .classroom import Classroom
from ..base import Base


__all__ = ("ClassInvite",)

class ClassInvite(Base):
    __tablename__ = 'classinvites'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    invite_code = Column(String, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    changed_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    class_id = Column(Integer, ForeignKey(Classroom.id), nullable=False)
    works_end = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    creator_id = Column(Integer, ForeignKey(User.id), nullable=False)
    invites_last = Column(Integer, default=1000000, nullable=False)
