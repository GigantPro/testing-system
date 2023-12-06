from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator

from .course_data import ReadCourseDataModel

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
    changed_time: datetime
    is_active: bool
    passing_id: list
    passed_id: list
    reviews: list
    rating: float
    course_data_id: int
    course_data: Optional[ReadCourseDataModel]

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
    changed_time: datetime
    is_active: bool
    reviews_count: int = Field(alias='reviews')
    passing_count: int = Field(alias='passing_id')
    passed_count: int = Field(alias='passed_id')
    rating: float

    role: Optional[str]
    course_type: str = 'read'

    @validator('reviews_count', 'passing_count', 'passed_count', pre=True)
    def validation_counts(cls, value):  # noqa: N805, ANN201, ANN001
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
    changed_time: datetime
    is_active: bool
    reviews: list
    course_data_id: int
    course_data: Optional[ReadCourseDataModel]
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


class CourseCreateModel(BaseModel):
    class Config:
        orm_mode = True

    title: str
    description: str
