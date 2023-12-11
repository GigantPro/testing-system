from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth import current_active_verified_user
from src.database import User, get_async_session
from src.functions import upload_solution_func
from src.types import CreateSolutionModel, ReadSolutionModel

from ..const import LANG_TO_SUFF
from ..router import solution_router

__all__ = ("upload_solution",)

@solution_router.post("/upload")
async def upload_solution(
    new_solution: CreateSolutionModel,
    user: User = Depends(current_active_verified_user),
    session: AsyncSession = Depends(get_async_session),
) -> ReadSolutionModel:
    return await upload_solution_func(new_solution, user, session, LANG_TO_SUFF)
