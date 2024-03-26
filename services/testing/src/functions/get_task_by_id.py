from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Task
from src.types import ReadTaskModel

from .secret_validate import secret_validate

__all__ = ("get_task_by_id",)

async def get_task_by_id(
    task_id: int,
    secret: str,
    session: AsyncSession,
) -> ReadTaskModel:
    if not await secret_validate(secret):
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})
    res = await session.get(Task, task_id)
    return res
