from sqlalchemy import JSON, TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql import func

from src.types import ExtraParamsModel

from ..base import Base

__all__ = ("Solution",)

class Solution(Base):
    __tablename__ = 'solutions'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    changed_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    created_time = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    task_id = Column(Integer, ForeignKey('task.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    code_url = Column(String, nullable=False)
    language = Column(String, nullable=False)

    status = Column(String, default='created', nullable=False)
    result = Column(String, nullable=True)

    testing_task_id = Column(Integer, nullable=True)
    correct = Column(Boolean, nullable=True)
    incorrect_log = Column(String, nullable=True)

    extra_params = Column(JSON, default=ExtraParamsModel().dict(), nullable=False)
