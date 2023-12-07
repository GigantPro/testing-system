from fastapi import Depends
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.functions import get_task_by_id
from src.types import ReadTaskModel

from ..router import tasks_api_router

__all__ = ("task_by_id",)

@tasks_api_router.get('/task_by_id')
async def task_by_id(
    task_id: int,
    secret: str,
    session: AsyncSession = Depends(get_async_session),
) -> ReadTaskModel:
    logger.info(f"Getting task: {task_id}")
    return await get_task_by_id(task_id, secret, session)
