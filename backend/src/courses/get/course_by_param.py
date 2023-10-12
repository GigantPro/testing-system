from typing import Any

from fastapi import Query
from fastapi.responses import JSONResponse

from ..router import courses_router
from src.functions import get_course_by_param
from src.types import CourseFullModel


__all__ = ("course_by_param",)

@courses_router.get('/course_by/{param}')
async def course_by_param(
    value: Any = Query(
        title='Value of param to fetch course',
        example=0,
    ),
    param: str = Query(
        default='id',
        title='Param to fetch course',
        description='Param must be on of thees: [id, title]',
        example=['id', 'title']
    )
) -> CourseFullModel:
    if param not in ('id', 'title'):
        return JSONResponse({'message': 'error'}, status_code=400)

    course = await get_course_by_param(param, value)

    if course:
        return course

    return JSONResponse(
        {'message': 'error'},
        status_code=400,
    )
