from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from .secret_validate import secret_validate
from src.database import Task
from src.types import ReadTaskModel, UpdateTaskModel


async def update_task(
    updated_task: UpdateTaskModel,
    task_id: int,
    secret: str,
    session: AsyncSession,
) -> ReadTaskModel:
    if not await secret_validate(secret):
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})

    try:
        task = (await session.scalars(select(Task).where(Task.id == task_id))).one()
    except NoResultFound:
        return JSONResponse(status_code=404, content={'message': 'Task not found'})

    for key, value in updated_task.model_dump().items():
        if value:
            setattr(task, key, value)

    await session.commit()
    await session.refresh(task)

    return ReadTaskModel(**task.__dict__)
