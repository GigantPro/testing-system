from typing import Optional
from datetime import datetime

from pydantic import BaseModel, json


__all__ = (
    "CourseFullModel",
    "CourseUserReadModel",
    "CourseWithDataModel",
    "CourseUpdateModel",
    "CourseCreateModel",
)

class CourseFullModel(BaseModel):
    id: int
    titele: str
    description: str
    ico_url: Optional[str]
    teachers_ids: json
    created_at: datetime
    is_active: bool
    passing_id: json
    passed_id: json
    reviews: json
    rating: float
    course_data: json
    course_type: str = 'full'


class CourseUserReadModel(BaseModel):
    id: int
    titele: str
    description: str
    ico_url: Optional[str]
    teachers_ids: json
    created_at: datetime
    is_active: bool
    reviews: json
    rating: float
    course_type: str = 'read'


class CourseWithDataModel(BaseModel):
    id: int
    titele: str
    description: str
    ico_url: Optional[str]
    teachers_ids: json
    created_at: datetime
    is_active: bool
    reviews: json
    course_data: json
    rating: float
    course_type: str = 'WithData'


class CourseUpdateModel(BaseModel):
    id: int
    titele: str
    description: str
    ico_url: Optional[str]
    teachers_ids: json
    is_active: bool
    course_data: json


class CourseCreateModel(BaseModel):
    titele: str
    description: str
