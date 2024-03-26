from fastapi import Depends
from fastapi.responses import FileResponse

from src.auth import current_active_verified_user
from src.database import User
from src.functions import get_solution_func

from ..router import solution_router

__all__ = ("get_solution",)

@solution_router.get("/download/{solution_name}")
async def get_solution(
    solution_name: str,
    user: User = Depends(current_active_verified_user),
) -> FileResponse:
    return await get_solution_func(solution_name, user)
