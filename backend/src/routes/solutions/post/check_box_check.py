from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth import current_active_verified_user
from src.database import User, get_async_session
from src.functions import check_box_check_func
from src.types import CreateSimpleSolutionModel, ReadSimpleSolutionModel

from ..const import LANG_TO_SUFF
from ..router import solution_router

__all__ = ("check_box_check",)

@solution_router.post("/check_box_check")
async def check_box_check(
    new_solution: CreateSimpleSolutionModel,
    user: User = Depends(current_active_verified_user),
    session: AsyncSession = Depends(get_async_session),
) -> ReadSimpleSolutionModel:
    return await check_box_check_func(new_solution, user, session)
