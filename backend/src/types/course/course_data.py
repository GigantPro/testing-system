from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from .module import FullModuleModel, ReadModuleModel


__all__ = (
    "CourseDataModel",
)

class FullCourseDataModel(BaseModel):
    id: int
    changed_time: datetime
    created_time: datetime
    modules: Optional[list[FullModuleModel]]


class ReadCourseDataModel(BaseModel):
    id: int
    changed_time: datetime
    created_time: datetime
    modules: Optional[list[ReadModuleModel]]
