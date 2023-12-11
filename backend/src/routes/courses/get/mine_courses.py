from fastapi import Depends, Query
from loguru import logger

from src.auth import current_active_verified_user
from src.database import User
from src.functions import get_courses_by_role
from src.types import CourseUserReadModel

from ..router import courses_router

__all__ = ("mine_courses",)

@courses_router.get('/me/where_am_i')
async def mine_courses(
    role: str = Query(
        default='student',
        title='The role of the user (student | teacher | all)',
        description='Will return the courses of the user',
    ),
    user: User = Depends(current_active_verified_user)
) -> list[CourseUserReadModel]:
    logger.info(f"Get mine courses: {role} from {user.id}")
    courses = await get_courses_by_role(role, user)
    return courses
