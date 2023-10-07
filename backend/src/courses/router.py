from typing import Any

from fastapi import APIRouter, Depends, Query, Form
from fastapi.responses import JSONResponse

from ..database import User
from src.functions import (
    get_course_by_id as func_get_course_by_id,
    create_new_course,
    get_course_by_param_func,
    get_top_of_courses,
    get_courses_by_role,
)
from src.const import current_active_verified_user
from src.types import CourseUserReadModel, CourseFullModel


__all__ = (
    "courses_router",
    "get_course_by_id",
    "get_course_by_param",
    "get_popular_courses",
    "get_mine_courses",
    "create_course",
)

courses_router = APIRouter(prefix='/course')


@courses_router.get('/get/{course_id}')
async def get_course_by_id(course_id: int):
    course = await func_get_course_by_id(course_id)
    return course


@courses_router.get('/course_by/{param}')
async def get_course_by_param(
    value: Any = Query(
        title='Value of param to fetch course',
        example=0,
    ),
    param: str = Query(
        default='id',
        title='Param to fetch course',
        description='Param must be on of thees: [id, titel]',
        example=['id', 'titel']
    )
) -> CourseFullModel:
    if param not in ('id', 'titel'):
        return JSONResponse({'message': 'error'}, status_code=400)

    course = await get_course_by_param_func(param, value)

    print(course)
    if course:
        return course

    return JSONResponse(
        {'message': 'error'},
        status_code=400,
    )


@courses_router.get('/most_popular')
async def get_popular_courses(
    count: int = Query(
        default=10,
        title='Count of returned courses',
        description='Count of returned courses. Must be <= 50 and > 0',
    ),
) -> list[CourseUserReadModel]:
    if count > 50 or count <= 0:
        return JSONResponse({'message': 'error'}, 400)

    top_courses = await get_top_of_courses(count)
    return [CourseUserReadModel.from_orm(course) for course in top_courses]


@courses_router.get('/me/where_am_i')
async def get_mine_courses(
    role: str = Query(
        default='student',
        title='The role of the user (student | teacher | all)',
        description='Will return the courses of the user',
    ),
    user: User = Depends(current_active_verified_user)
) -> list[CourseUserReadModel]:
    courses = await get_courses_by_role(role, user)
    return courses


@courses_router.post('/create')
async def create_course(
    title: str = Form(),
    description: str = Form(),
    user: User = Depends(current_active_verified_user),
) -> JSONResponse:
    await create_new_course(title, description, user)
    return JSONResponse({'message': 'success'}, 200)
