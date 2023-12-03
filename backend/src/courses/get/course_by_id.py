from src.functions import get_course_by_id
from src.types import CourseFullModel

from ..router import courses_router

__all__ = ("course_by_id",)

@courses_router.get('/get/{course_id}')
async def course_by_id(course_id: int) -> CourseFullModel:
    course = await get_course_by_id(course_id)
    return course
