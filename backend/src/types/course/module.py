from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from .task import TaskModel


__all__ = (
    "ModuleModel",
)

class ModuleModel(BaseModel):
    id: int
    changed_time: datetime
    created_time: datetime
    tasks: Optional[list[TaskModel]]
