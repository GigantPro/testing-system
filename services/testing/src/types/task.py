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
    class Config:
        orm_mode = True
        from_attributes = True

    id: int
    user_id: int

    testing_mode: str
    status: str

    url_code_for_run: Optional[str]
    s_code_for_run: Optional[str]
    code_languge: str

    created_at: datetime
    updated_at: datetime

    priority: int


class ReadTaskModel(FullTaskModel):
    pass


class CreateTaskModel(BaseModel):
    user_id: int
    testing_mode: str
    url_code_for_run: Optional[str]
    s_code_for_run: Optional[str]
    code_languge: str
    priority: Optional[int]

class UpdateTaskModel(BaseModel):
    testing_mode: Optional[str]
    url_code_for_run: Optional[str]
    s_code_for_run: Optional[str]
    code_languge: Optional[str]
    priority: Optional[int]
