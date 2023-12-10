import hashlib

import aiofiles
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import config
# from src.const.lang_to_suff import LANG_TO_SUFF
from src.database import Solution, Task, User
from src.types import CreateSolutionModel, ReadSolutionModel

__all__ = ("upload_solution_func",)

async def upload_solution_func(
    new_solution: CreateSolutionModel,
    user: User,
    session: AsyncSession,
    LANG_TO_SUFF: dict[str, str],
) -> ReadSolutionModel:
    if new_solution.language not in LANG_TO_SUFF:
        return JSONResponse(status_code=400, content={'message': 'Invalid language'})

    hash = hashlib.md5(new_solution.code.encode()).hexdigest()
    async with aiofiles.open(
        f"{config.static_files_path}/solutions/{hash}.{LANG_TO_SUFF[new_solution.language]}", "w"
    ) as f:
        f.write(new_solution.code.encode())

    session.begin()

    try:
        task: Task = (await session.scalars(select(Task).where(Task.id == new_solution.task_id))).one()
    except NoResultFound:
        return JSONResponse(status_code=404, content={'message': 'Task not found'})

    sol = Solution(
        user_id=user.id,
        code=new_solution.code,
        language=new_solution.language,
        code_language=new_solution.language,
        task_id=new_solution.task_id,
        extra_params=task.extra_params,
    )

    await session.add(sol)
    await session.refresh(sol)

    return ReadSolutionModel(**sol.__dict__)
