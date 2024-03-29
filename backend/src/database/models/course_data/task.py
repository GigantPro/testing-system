from sqlalchemy import JSON, TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.sql import func

from src.types.extra_params import ExtraParamsModel

from ...base import Base

__all__ = ("Task",)

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    changed_time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    created_time = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    module_id = Column(Integer, ForeignKey('modules.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    type = Column(Integer, nullable=False)
    """
    0 - text
    1 - video
    2 - test
    3 - radio test
    4 - checkbox test
    """
    title = Column(String, nullable=True)
    text = Column(String, nullable=True)
    description = Column(String, nullable=True)
    video_url = Column(String, nullable=True)
    tests_type = Column(Integer, nullable=True)
    """
    0 - simple test
    1 - simple test with extra code for main.py
    2 - test with random input data
    """
    simple_test_data = Column(JSON, nullable=True)
    """
    {'test_input': 'solution_output'}
    """
    box_solutions = Column(JSON, nullable=True)
    solution = Column(String, nullable=True)
    solution_for_testing = Column(String, nullable=True)

    extra_params = Column(JSON, default=ExtraParamsModel().dict(), nullable=False)
