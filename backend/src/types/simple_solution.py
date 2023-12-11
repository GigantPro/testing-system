from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .extra_params import ExtraParamsModel

__all__ = (
    "FullSimpleSolutionModel",
    "CreateSimpleSolutionModel",
    "ReadSimpleSolutionModel",
    "UpdateSimpleSolutionModel",
)


class FullSimpleSolutionModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    created_time: datetime
    changed_time: datetime

    task_id: int
    user_id: int

    answer: dict
    
    correct: bool


class CreateSimpleSolutionModel(BaseModel):
    task_id: int
    answer: dict


class ReadSimpleSolutionModel(FullSimpleSolutionModel):
    pass


class UpdateSimpleSolutionModel(BaseModel):
    answer: dict
