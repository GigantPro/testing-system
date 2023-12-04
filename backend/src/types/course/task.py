from datetime import datetime
from typing import Optional

from pydantic import BaseModel

__all__ = (
    "FullTaskModel",
    "ReadTaskModel",
    "CreateTaskModel",
    "UpdateTaskModel",
)

class FullTaskModel(BaseModel):
    id: int
    changed_time: datetime
    created_time: datetime
    type: int
    title: Optional[str]
    text: Optional[str]
    description: Optional[str]
    video_url: Optional[str]
    tests_type: Optional[int]
    simple_test_data: Optional[dict]
    solution: Optional[str]
    solution_for_testing: Optional[str]


class ReadTaskModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    changed_time: datetime
    created_time: datetime
    type: int
    title: Optional[str]
    text: Optional[str]
    description: Optional[str]
    video_url: Optional[str]
    tests_type: Optional[int]

class CreateTaskModel(BaseModel):
    type: int
    title: Optional[str]
    text: Optional[str]
    description: Optional[str]
    video_url: Optional[str]
    tests_type: Optional[int]
    simple_test_data: Optional[dict]
    solution: Optional[str]
    solution_for_testing: Optional[str]

class UpdateTaskModel(CreateTaskModel):
    pass
