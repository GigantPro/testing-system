from fastapi import Query
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from loguru import logger

from src.functions import get_top_of_courses
from src.types import CourseUserReadModel

from ..router import courses_router

__all__ = ("popular_courses",)

@courses_router.get('/most_popular')
async def popular_courses(
    request: Request,
    start_index: int = Query(
        default=0,
        title='Start inxed for popular courses',
        description='Will return courses from this index',
    ),
    count: int = Query(
        default=10,
        title='Count of returned courses',
        description='Count of returned courses. Must be <= 50 and > 0',
    ),
) -> list[CourseUserReadModel]:
    logger.info(f"Get popular courses from {start_index} count {count} from {request.client.host}")
    if count > 50 or count <= 0:
        return JSONResponse({'message': 'error'}, 400)

    top_courses = await get_top_of_courses(start_index, count)
    return [CourseUserReadModel.from_orm(course) for course in top_courses]
