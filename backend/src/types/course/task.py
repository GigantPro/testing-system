from datetime import datetime
from typing import Optional

from loguru import logger
from pydantic import BaseModel, Field, validator

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
    course_id: int
    module_id: int
    title: Optional[str]
    text: Optional[str]
    description: Optional[str]
    video_url: Optional[str]
    tests_type: Optional[int]
    simple_test_data: Optional[dict]
    box_solutions: Optional[dict]
    solution: Optional[str]
    solution_for_testing: Optional[str]


class ReadTaskModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    changed_time: datetime
    created_time: datetime
    type: int
    course_id: int
    module_id: int
    title: Optional[str]
    text: Optional[str]
    description: Optional[str]
    video_url: Optional[str]
    tests_type: Optional[int]
    box_task: Optional[list] = Field(alias="box_solutions")

    @validator("box_task", pre=True)
    def validate_box_task(cls, v: dict):  # noqa: N805, ANN201
        logger.warning(f'{v=}|{type(v)=}')
        if v is None:
            return None

        if isinstance(v, list):
            return v

        return (list(v.keys()))


class CreateTaskModel(BaseModel):
    type: int
    title: Optional[str]
    text: Optional[str]
    description: Optional[str]
    video_url: Optional[str]
    tests_type: Optional[int]
    simple_test_data: Optional[dict]
    box_solutions: Optional[dict]
    solution: Optional[str]
    solution_for_testing: Optional[str]

class UpdateTaskModel(CreateTaskModel):
    type: Optional[int]
