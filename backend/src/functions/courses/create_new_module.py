from fastapi.responses import JSONResponse
from sqlalchemy import update, select

from src.database import engine, Course, User
from src.types import CreateModuleModel


__all__ = ("create_new_module",)

async def create_new_module(course_id: int, new_module: CreateModuleModel, user: User) -> JSONResponse:
    async with engine.connect() as connection:
        res = await connection.execute(
            select(Course)
            .where(Course.id == course_id)
        ).fetchone()
        
        print(res)
        
        await connection.commit()
