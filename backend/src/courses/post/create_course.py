from fastapi import Depends, Form
from fastapi.responses import JSONResponse

from src.functions import create_new_course
from src.database import User
from src.const import current_active_verified_user
from src.types import CourseUserReadModel
from ..router import courses_router


__all__ = ("create_course",)

@courses_router.post('/create')
async def create_course(
    title: str = Form(),
    description: str = Form(),
    user: User = Depends(current_active_verified_user),
) -> CourseUserReadModel:
    new_course = await create_new_course(title, description, user)
    return new_course
