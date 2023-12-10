from fastapi import Depends
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth import current_active_verified_user
from src.database import User, get_async_session
from src.functions import create_new_task
from src.types import CreateTaskModel, ReadTaskModel

from ..router import courses_router

__all__ = ("create_task",)

@courses_router.post('/task/create', tags=['task'])
async def create_task(
    new_task: CreateTaskModel,
    module_id: int,
    course_id: int,
    user: User = Depends(current_active_verified_user),
    session: AsyncSession = Depends(get_async_session),
) -> ReadTaskModel:
    logger.info(f"Create new task: {module_id=} {course_id=} from {user.id}")
    return await create_new_task(new_task, module_id, course_id, user, session)
