from fastapi import Query
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from loguru import logger

from src.database import Course, json_array_length
from src.functions import get_top_of_courses, get_top_of_courses_by
from src.types import CourseUserReadModel

from ..router import courses_router

__all__ = ("popular_courses_by",)

dict_ = {
    'rating':        Course.__table__.c.rating.desc(),
    'created_time':  Course.__table__.c.created_at.desc(),
    'reviews_count': json_array_length(Course.__table__.c.reviews).desc(),
    'passed_count':  json_array_length(Course.__table__.c.passed_id).desc(),
    'passing_count': json_array_length(Course.__table__.c.passing_id).desc(),
    'popularity': None
}

@courses_router.get('/popular_by')
async def popular_courses_by(
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
    by_: str = Query(
        title='The parameter by which you need to get filtered snare',
        description='Must be one of thees: [created_time, passed_count, '
                    'passing_count, reviews_count, rating, popularity]',
    ),
) -> list[CourseUserReadModel]:
    logger.info(f"Get popular courses by {by_} from {start_index} count {count} from {request.client.host}")
    if count > 50 or count <= 0 or by_ not in dict_:
        return JSONResponse({'message': 'error'}, 401)

    if by_ == 'popular':
        return await get_top_of_courses(start_index, count)

    return [CourseUserReadModel.from_orm(course) for course in \
        await get_top_of_courses_by(start_index, count, dict_[by_])]
