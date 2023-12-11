from fastapi import Depends
from fastapi.requests import Request
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth import current_active_verified_user
from src.database import User, get_async_session
from src.functions import update_task as update_task_func
from src.types import ReadTaskModel, UpdateTaskModel

from ..router import courses_router

__all__ = ("update_task",)

@courses_router.patch('/task/update', tags=['task'])
async def update_task(
    updated_task: UpdateTaskModel,
    task_id: int,
    request: Request,
    user: User = Depends(current_active_verified_user),
    session: AsyncSession = Depends(get_async_session),
) -> ReadTaskModel:
    logger.info(f"Update task: {task_id} from {user.id} from {request.client.host}")
    return await update_task_func(updated_task, task_id, user, session)
