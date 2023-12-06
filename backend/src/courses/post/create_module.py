from fastapi import Depends
from fastapi.responses import JSONResponse

from src.const import current_active_verified_user
from src.database import User
from src.functions import create_new_module
from src.types import CreateModuleModel

from ..router import courses_router

__all__ = ("create_course_module",)

@courses_router.post('/module/create')
async def create_course_module(
    new_module: CreateModuleModel,
    course_id: int,
    user: User = Depends(current_active_verified_user),
) -> JSONResponse:
    return await create_new_module(course_id, new_module, user)
