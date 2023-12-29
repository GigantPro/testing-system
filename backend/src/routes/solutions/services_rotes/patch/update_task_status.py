from fastapi import Depends
from fastapi.responses import JSONResponse
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth import current_active_verified_user
from src.database import User, get_async_session
from src.types import ServiceTaskModel
from src.solutions_engine import solutions_engine

from ..router import services_router
from ..funcs import secret_validate

__all__ = ("update_task_status",)

@services_router.post("/update_task_status")
async def update_task_status(
    updated_task: ServiceTaskModel,
    secret: str,
) -> None:
    logger.info(f'Updating task status: {updated_task.id=}')
    if not await secret_validate(secret):
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})

    for sol_id in solutions_engine.checking_solutions:
        if updated_task.id in solutions_engine.checking_solutions[sol_id]['tasks_ids']:
            solutions_engine.checking_solutions[sol_id]['tasks'].append(updated_task)
            break
