from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field, validator

from .course_data import CourseDataModel


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
    course_data: Optional[CourseDataModel]

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
    reviews_count: int = Field(alias='reviews')
    passing_count: int = Field(alias='passing_id')
    passed_count: int = Field(alias='passed_id')
    rating: float

    role: Optional[str]
    course_type: str = 'read'

    @validator('reviews_count', 'passing_count', 'passed_count', pre=True)
    def validation_counts(cls, value):  # noqa: N805
        if isinstance(value, int):
            return value
        return len(value)


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
    course_data: Optional[CourseDataModel]
    rating: float

    role: Optional[str]
    course_type: str = 'WithData'


class CourseUpdateModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    title: Optional[str]
    description: Optional[str]
    ico_url: Optional[str]
    teachers_ids: Optional[list[int]]
    is_active: Optional[bool]
    course_data: Optional[CourseDataModel]


class CourseCreateModel(BaseModel):
    class Config:
        orm_mode = True

    title: str
    description: str
