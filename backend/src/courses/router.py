from typing import Any

from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse

from ..auth.database import User
from ..auth.auth import fastapi_users
from .functions import (
    get_course_by_id,
    create_new_course,
    get_course_by_param,
)


current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

courses_router = APIRouter(prefix='/course')


@courses_router.get('/{id}')
async def get_course(id: int) -> dict:
    course = await get_course_by_id(id)
    return {
        'id': course.id,
        'owners': course.owners_ids,
        'titel': course.title,
        'description': course.description,
        'created_at': course.created_at,
        'is_active': course.is_active,
        'course_data': course.course_data,
    }


@courses_router.get('/course_by/{param}')
async def get_course(
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
) -> dict:
    if param not in ('id', 'titel'):
        return JSONResponse({'message': 'error'}, status_code=400)

    course = await get_course_by_param(param, value)
    
    if course:
        return {
            'id': course.id,
            'owners': course.owners_ids,
            'titel': course.title,
            'description': course.description,
            'created_at': course.created_at,
            'is_active': course.is_active,
            'course_data': course.course_data,
        }
    return JSONResponse(
        {'message': 'error'},
        status_code=400,
    )


@courses_router.post('/create')
async def create_course(title: str, description: str, user: User = Depends(current_active_verified_user)) -> Any:
    await create_new_course(title, description, user)

    return None
