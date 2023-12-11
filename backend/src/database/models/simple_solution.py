from sqlalchemy import JSON, TIMESTAMP, Boolean, Column, ForeignKey, Integer
from sqlalchemy.sql import func

from ..base import Base

__all__ = ("SimpleSolution",)

class SimpleSolution(Base):
    __tablename__ = 'simple_solutions'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    changed_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    created_time = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    task_id = Column(Integer, ForeignKey('task.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    answer = Column(JSON, nullable=False)

    correct = Column(Boolean, nullable=True)
