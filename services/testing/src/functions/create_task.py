from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import config
from src.database import Task
from src.types import CreateTaskModel, ReadTaskModel

__all__ = ("create_task",)

async def create_task(
    new_task: CreateTaskModel,
    secret: str,
    session: AsyncSession,
) -> ReadTaskModel:
    if secret != config.tests_api_secret:
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})
    session.begin()

    task = Task(**new_task.model_dump())

    session.add(task)

    await session.commit()
    await session.refresh(task)

    return ReadTaskModel.from_orm(task)
