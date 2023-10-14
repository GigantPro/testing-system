from fastapi import Query
from fastapi.responses import JSONResponse

from ..router import courses_router
from src.functions import get_top_of_courses
from src.types import CourseUserReadModel


__all__ = ("popular_courses",)

@courses_router.get('/most_popular')
async def popular_courses(
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
    if count > 50 or count <= 0:
        return JSONResponse({'message': 'error'}, 400)

    top_courses = await get_top_of_courses(start_index, count)
    return [CourseUserReadModel.from_orm(course) for course in top_courses]
