from datetime import datetime

from pydantic import BaseModel

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
