from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .extra_params import ExtraParamsModel

__all__ = (
    "FullTaskModel",
    "ReadTaskModel",
    "CreateTaskModel",
    "UpdateTaskModel",
)

class FullTaskModel(BaseModel):
    class Config:
        from_attributes = True
        from_orm = True

    id: int
    user_id: int

    status: str

    url_code_for_run: Optional[str] = Field(None, nullable=True)
    code_languge: str

    correct_output: Optional[str] = Field(None, nullable=True)
    correct: Optional[str] = Field(None, nullable=True)
    incorrect_log: Optional[str] = Field(None, nullable=True)

    created_at: datetime
    updated_at: datetime

    priority: int

    extra_params: ExtraParamsModel


class ReadTaskModel(FullTaskModel):
    pass


class CreateTaskModel(BaseModel):
    user_id: int
    url_code_for_run: Optional[str] = Field(None, nullable=True)
    code_languge: str
    correct_output: Optional[str] = Field(None, nullable=True)
    priority: Optional[int] = Field(None, nullable=True)
    extra_params: Optional[ExtraParamsModel] = Field(ExtraParamsModel(), nullable=False)


class UpdateTaskModel(BaseModel):
    url_code_for_run: Optional[str] = Field(None, nullable=True)
    correct_output: Optional[str] = Field(None, nullable=True)
    code_languge: Optional[str] = Field(None, nullable=True)
    priority: Optional[int] = Field(None, nullable=True)
    extra_params: Optional[ExtraParamsModel] = Field(ExtraParamsModel(), nullable=False)
