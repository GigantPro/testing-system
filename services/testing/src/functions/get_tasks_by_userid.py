from typing import Optional

from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Task
from src.types import ReadTaskModel

from .secret_validate import secret_validate

__all__ = ("get_tasks_by_userid",)

async def get_tasks_by_userid(
    user_id: int,
    filter: Optional[str],
    secret: str,
    session: AsyncSession,
    limit: int = 20,
) -> list[ReadTaskModel]:
    if not await secret_validate(secret):
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})

    if filter:
        res =  (await session.execute(
            select(Task)
            .where(Task.user_id == user_id)
            .where(Task.status == filter)
            .order_by(Task.created_at.desc(), reversed=True)
            .limit(limit)
        )).all()

        for i in range(len(res)):
            res[i] = ReadTaskModel.from_orm(res[i][0])

        return res

    res =  (await session.execute(
        select(Task)
        .where(Task.user_id == user_id)
        .order_by(Task.created_at.desc(), reversed=True)
        .limit(limit)
    )).all()

    for i in range(len(res)):
        res[i] = ReadTaskModel.from_orm(res[i][0])

    return res
