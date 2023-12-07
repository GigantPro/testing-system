from typing import Optional

from fastapi import Depends, Query
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.functions import get_tasks_by_userid
from src.types import ReadTaskModel

from ..router import tasks_api_router

__all__ = ("tasks_by_userid",)

@tasks_api_router.get('/tasks_by_userid')
async def tasks_by_userid(
    user_id: int,
    secret: str,
    filter: Optional[str] = Query(
        title='Filter for sorting by status { created; processing; completed; }',
        example='created',
        default=None
    ),
    limit: int = Query(
        title='Count of returned params',
        example=100,
        default=20
    ),
    session: AsyncSession = Depends(get_async_session),
) -> list[ReadTaskModel]:
    logger.info(f"Getting task: {user_id} whith filter: {filter} and offset: {limit}")
    return await get_tasks_by_userid(user_id, filter, secret, session, limit=limit)
