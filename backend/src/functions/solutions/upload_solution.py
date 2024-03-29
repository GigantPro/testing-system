import hashlib

import aiofiles
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import config
from src.database import Solution, Task, User
from src.types import CreateSolutionModel, ReadSolutionModel

__all__ = ("upload_solution_func",)

async def upload_solution_func(
    new_solution: CreateSolutionModel,
    user: User,
    session: AsyncSession,
    lang_to_suff: dict[str, str],
) -> ReadSolutionModel:
    if new_solution.language not in lang_to_suff:
        return JSONResponse(status_code=400, content={'message': 'Invalid language'})
    session.begin()

    try:
        task: Task = (await session.scalars(select(Task).where(Task.id == new_solution.task_id))).one()
    except NoResultFound:
        return JSONResponse(status_code=404, content={'message': 'Task not found'})

    hash = hashlib.md5(new_solution.code.encode()).hexdigest()
    async with aiofiles.open(
        f"{config.solutions_files_path}/{user.id}{hash}.{lang_to_suff[new_solution.language]}", "w"
    ) as f:
        await f.write(new_solution.code)


    sol = Solution(
        user_id=user.id,
        code_url=f'/{config.solutions_files_path}/download/{user.id}{hash}.{lang_to_suff[new_solution.language]}',
        language=new_solution.language,
        task_id=new_solution.task_id,
        extra_params=task.extra_params,
    )

    session.add(sol)
    await session.commit()
    await session.refresh(sol)

    return ReadSolutionModel(**sol.__dict__)
