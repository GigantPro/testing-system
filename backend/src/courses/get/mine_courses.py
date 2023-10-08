from fastapi import Query, Depends

from ..router import courses_router
from src.functions import get_courses_by_role
from src.database import User
from src.types import CourseUserReadModel
from src.const import current_active_verified_user


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
    courses = await get_courses_by_role(role, user)
    return courses
