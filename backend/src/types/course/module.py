from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .task import FullTaskModel, ReadTaskModel

__all__ = (
    "FullModuleModel",
    "ReadModuleModel",
    "CreateModuleModel",
)

class FullModuleModel(BaseModel):
    class Config:
        orm_mode = True
    
    id: int
    changed_time: datetime
    created_time: datetime
    title: str
    description: Optional[str]
    tasks: Optional[list[FullTaskModel]]
    course_id: int

class ReadModuleModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    changed_time: datetime
    created_time: datetime
    tasks: Optional[list[ReadTaskModel]]
    course_id: int

class CreateModuleModel(BaseModel):
    title: str
    description: Optional[str]
