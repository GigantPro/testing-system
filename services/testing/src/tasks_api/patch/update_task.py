from fastapi import Body, Depends
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.functions import update_task as update_task_func
from src.types import ReadTaskModel, UpdateTaskModel

from ..router import tasks_api_router

__all__ = ("task_update",)

@tasks_api_router.patch('/update_task')
async def task_update(
    updated_task: UpdateTaskModel,
    task_id: int = Body(...),
    secret: str = Body(...),
    session: AsyncSession = Depends(get_async_session),
) -> ReadTaskModel:
    logger.info(f"Updating task: {task_id}")
    return await update_task_func(updated_task, task_id, secret, session)
