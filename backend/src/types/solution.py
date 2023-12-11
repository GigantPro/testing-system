from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .extra_params import ExtraParamsModel

__all__ = (
    "FullSolutionModel",
    "CreateSolutionModel",
    "ReadSolutionModel",
    "UpdateSolutionModel",
)


class FullSolutionModel(BaseModel):
    id: int
    created_time: datetime
    changed_time: datetime

    task_id: int
    user_id: int

    code_url: str
    language: str

    status: str
    result: Optional[str] = Field(None, nullable=True)

    testing_task_id: Optional[int] = Field(None, nullable=True)
    correct: Optional[bool] = Field(None, nullable=True)
    incorrect_log: Optional[str] = Field(None, nullable=True)

    extra_params: ExtraParamsModel


class CreateSolutionModel(BaseModel):
    task_id: int
    code: str
    language: str


class ReadSolutionModel(BaseModel):
    id: int
    created_time: datetime
    changed_time: datetime

    task_id: int
    user_id: int

    code_url: str
    language: str

    status: str
    result: Optional[str] = Field(None, nullable=True)

    testing_task_id: Optional[int] = Field(None, nullable=True)
    correct: Optional[bool] = Field(None, nullable=True)
    incorrect_log: Optional[str] = Field(None, nullable=True)

    extra_params: ExtraParamsModel


class UpdateSolutionModel(BaseModel):
    result: Optional[str] = Field(None, nullable=True)
    testing_task_id: Optional[int] = Field(None, nullable=True)
    correct: Optional[bool] = Field(None, nullable=True)
    incorrect_log: Optional[str] = Field(None, nullable=True)
