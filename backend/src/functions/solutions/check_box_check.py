from pathlib import Path
from fastapi.responses import FileResponse, JSONResponse
from loguru import logger
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import config
from src.database import User, SimpleSolution, Task
from src.types import CreateSimpleSolutionModel, ReadSimpleSolutionModel

__all__ = ("check_box_check_func",)

async def check_box_check_func(
    new_solution: CreateSimpleSolutionModel,
    user: User,
    session: AsyncSession,
) -> ReadSimpleSolutionModel:
    session.begin()

    try:
        task: Task = (await session.scalars(select(Task).where(Task.id == new_solution.task_id))).one()
    except NoResultFound:
        return JSONResponse(status_code=404, content={'message': 'Task not found'})

    if task.type not in (3, 4):
        return JSONResponse(status_code=400, content={'message': 'Wrong task type'})

    solution = SimpleSolution(
        task_id=new_solution.task_id,
        user_id=user.id,
        answer=new_solution.answer,
        correct=(task.box_solutions == new_solution.answer),
    )
    
    session.add(solution)
    await session.commit()
    await session.refresh(solution)
    
    return ReadSimpleSolutionModel.from_orm(solution)
