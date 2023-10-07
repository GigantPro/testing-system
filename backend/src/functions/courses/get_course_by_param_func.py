from typing import Any

from loguru import logger
from sqlalchemy import select

from src.database import engine, Course


__all__ = ("get_course_by_param_func",)

async def get_course_by_param_func(param: str, value: Any) -> Course:
    if param == 'id':
        value = int(value)
    logger.warning(f'{param=}, {value=}')
    async with engine.connect() as connection:
        db_answer = await connection.execute(select(Course).where(param == value))
        return db_answer.fetchone()
