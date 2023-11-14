from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from .task import FullTaskModel, ReadTaskModel


__all__ = (
    "ModuleModel",
    "ReadModuleModel",
)

class FullModuleModel(BaseModel):
    id: int
    changed_time: datetime
    created_time: datetime
    tasks: Optional[list[FullTaskModel]]

class ReadModuleModel(BaseModel):
    id: int
    changed_time: datetime
    created_time: datetime
    tasks: Optional[list[ReadTaskModel]]
