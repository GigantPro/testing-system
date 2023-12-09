from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Task
from src.types import CreateTaskModel, ReadTaskModel

from .secret_validate import secret_validate

__all__ = ("create_task",)

async def create_task(
    new_task: CreateTaskModel,
    secret: str,
    session: AsyncSession,
) -> ReadTaskModel:
    if not await secret_validate(secret):
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})
    session.begin()

    task = Task(**new_task.model_dump())

    session.add(task)

    await session.commit()
    await session.refresh(task)

    return ReadTaskModel.from_orm(task)
