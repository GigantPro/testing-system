from typing import Any

from sqlalchemy import select, insert
from loguru import logger

from ..auth.database import User
from .database import Course, engine


__all__ = (
    "get_course_by_id",
    "create_new_course",
    "get_course_by_id",
)

async def get_course_by_id(id: int) -> Course:
    async with engine.connect() as connection:
        db_answer = await connection.execute(select(Course).where(Course.id == id))
        return db_answer.fetchone()


async def create_new_course(title: str, description: str, user: User) -> int:
    async with engine.connect() as connection:
        await connection.execute(
            insert(Course)
            .values(
                owners_ids = [user.id],
                title = title,
                description = description,
            )
        )
        await connection.commit()
        
        ...  # Fix me: Добавить возвращение присвоенного id


async def get_course_by_param(param: str, value: Any) -> Course:
    if param == 'id': value = int(value)
    logger.warning(f'{param=}, {value=}')
    async with engine.connect() as connection:
        db_answer = await connection.execute(select(Course).where(param == value))
        return db_answer.fetchone()
