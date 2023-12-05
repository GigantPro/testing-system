from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Task
from src.types import ReadTaskModel

__all__ = ("get_task_by_id",)

async def get_task_by_id(task_id: int, session: AsyncSession) -> ReadTaskModel:
    try:
        task = (await session.scalars(select(Task).where(Task.id == task_id))).one()
        return ReadTaskModel.from_orm(task)
    except NoResultFound:
        return JSONResponse(status_code=404, content={"message": "Task not found"})
