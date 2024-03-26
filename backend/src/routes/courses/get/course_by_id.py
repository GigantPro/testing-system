from fastapi.requests import Request
from loguru import logger

from src.functions import get_course_by_id
from src.types import CourseUserReadModel

from ..router import courses_router

__all__ = ("course_by_id",)

@courses_router.get('/get/{course_id}')
async def course_by_id(course_id: int, request: Request) -> CourseUserReadModel:
    logger.info(f"Get course by id: {course_id} from {request.client.host}")
    course = await get_course_by_id(course_id)
    return course
