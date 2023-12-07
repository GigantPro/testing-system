from fastapi import Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.functions import create_task as create_task_func
from src.types import CreateTaskModel, ReadTaskModel

from ..router import tasks_api_router

__all__ = ("task_create",)

@tasks_api_router.post('/create_task')
async def task_create(
    new_task: CreateTaskModel,
    secret: str = Body(...),
    session: AsyncSession = Depends(get_async_session),
) -> ReadTaskModel:
    return await create_task_func(new_task, secret, session)
