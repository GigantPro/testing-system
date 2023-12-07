from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

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

    testing_mode: str
    status: str

    url_code_for_run: Optional[str] = Field(None, nullable=True)
    s_code_for_run: Optional[str] = Field(None, nullable=True)
    code_languge: str

    created_at: datetime
    updated_at: datetime

    priority: int


class ReadTaskModel(FullTaskModel):
    pass


class CreateTaskModel(BaseModel):
    user_id: int
    testing_mode: str
    url_code_for_run: Optional[str] = Field(None, nullable=True)
    s_code_for_run: Optional[str] = Field(None, nullable=True)
    code_languge: str
    priority: Optional[int] = Field(None, nullable=True)

class UpdateTaskModel(BaseModel):
    testing_mode: Optional[str] = Field(None, nullable=True)
    url_code_for_run: Optional[str] = Field(None, nullable=True)
    s_code_for_run: Optional[str] = Field(None, nullable=True)
    code_languge: Optional[str] = Field(None, nullable=True)
    priority: Optional[int] = Field(None, nullable=True)
