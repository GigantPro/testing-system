
from sqlalchemy import TIMESTAMP, Column, Integer, String, func

from ..base import Base

__all__ = ("Task",)

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, nullable=False)

    testing_mode = Column(String, nullable=False)
    status = Column(String, nullable=False, default='created')
    """{ created; processing; completed; }"""

    result = Column(String)
    build_output = Column(String)
    result_getted_time = Column(TIMESTAMP(timezone=True))

    url_code_for_run = Column(String)
    s_code_for_run = Column(String)
    code_languge = Column(String, nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    priority = Column(Integer, nullable=False, default=0)
