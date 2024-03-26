from fastapi import Depends
from fastapi.requests import Request
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.base import get_async_session
from src.functions import get_task_by_id
from src.types import ReadTaskModel

from ..router import courses_router

__all__ = ("task_by_id",)

@courses_router.get('/task/{task_id}', tags=['task'])
async def task_by_id(task_id: int, request: Request,
                     session: AsyncSession = Depends(get_async_session),) -> ReadTaskModel:
    logger.info(f"Get task by id: {task_id} from {request.client.host}")
    return await get_task_by_id(task_id, session)
