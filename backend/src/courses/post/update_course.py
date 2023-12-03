from fastapi import Depends
from fastapi.responses import JSONResponse

from src.const import current_active_verified_user
from src.database import User
from src.functions import update_course as update_course_func
from src.types import CourseUpdateModel

from ..router import courses_router

__all__ = ("update_course",)

@courses_router.post('/update')
async def update_course(
    updated_course: CourseUpdateModel,
    user: User = Depends(current_active_verified_user),
) -> JSONResponse:
    return await update_course_func(updated_course, user)
