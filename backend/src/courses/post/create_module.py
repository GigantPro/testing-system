from fastapi import Depends
from fastapi.responses import JSONResponse

from src.functions import update_course as update_course_func
from src.database import User
from src.types import FullModuleModel, CourseUpdateModel
from src.const import current_active_verified_user


__all__ = ("create_course_module",)

@courses_router.post('/module/create')
async def create_course_module(
    new_module: FullModuleModel,
    course_id: int,
    user: User = Depends(current_active_verified_user),
) -> JSONResponse:
    updated_course = CourseUpdateModel(
        id=course_id,
        modules=new_module
    )
    return await update_course_func(updated_course, user)
