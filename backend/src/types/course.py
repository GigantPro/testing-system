from typing import Optional
from datetime import datetime

from pydantic import BaseModel


__all__ = (
    "CourseFullModel",
    "CourseUserReadModel",
    "CourseWithDataModel",
    "CourseUpdateModel",
    "CourseCreateModel",
)

class CourseFullModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    title: str
    description: str
    ico_url: Optional[str]
    teachers_ids: list
    created_at: datetime
    is_active: bool
    passing_id: list
    passed_id: list
    reviews: list
    rating: float
    course_data: dict

    role: Optional[str]
    course_type: str = 'full'


class CourseUserReadModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    title: str
    description: str
    ico_url: Optional[str]
    teachers_ids: list
    created_at: datetime
    is_active: bool
    reviews: list
    rating: float

    role: Optional[str]
    course_type: str = 'read'


class CourseWithDataModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    title: str
    description: str
    ico_url: Optional[str]
    teachers_ids: list
    created_at: datetime
    is_active: bool
    reviews: list
    course_data: dict
    rating: float

    role: Optional[str]
    course_type: str = 'WithData'


class CourseUpdateModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    title: str
    description: str
    ico_url: Optional[str]
    teachers_ids: list
    is_active: bool
    course_data: dict


class CourseCreateModel(BaseModel):
    class Config:
        orm_mode = True

    title: str
    description: str
