from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from .module import ModuleModel


__all__ = (
    "CourseDataModel",
)

class CourseDataModel(BaseModel):
    id: int
    changed_time: datetime
    created_time: datetime
    modules: Optional[ModuleModel]
