from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

__all__ = (
    "FullCourseDataModel",
    "ReadCourseDataModel",
)

class FullCourseDataModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    changed_time: datetime
    created_time: datetime
    modules_ids: Optional[list[int]] = Field(alias='modules')


class ReadCourseDataModel(BaseModel):
    id: int
    changed_time: datetime
    created_time: datetime
    modules_ids: Optional[list[int]] = Field(alias='modules')
