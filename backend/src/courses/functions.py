from typing import Any

from sqlalchemy import select, insert
from loguru import logger

from ..auth.database import User
from .database import Course, engine


__all__ = (
    "get_course_by_id",
    "create_new_course",
    "get_course_by_id",
    "get_top_of_courses",
    "json_by_course_obj",
)

async def get_course_by_id(course_id: int) -> Course:
    async with engine.connect() as connection:
        db_answer = await connection.execute(select(Course).where(Course.id == course_id))
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


async def get_top_of_courses(count: int) -> list[Course]:
    async with engine.connect() as connection:
        db_answer = await connection.execute(
            select(Course)
            .where(Course.is_active == True)
            .order_by(Course.passed, Course.likes, Course.passing, Course.rating)
            .limit(count)
        )
        return db_answer


async def json_by_course_obj(course_obj: Course) -> list[Any]:
    return {
        'id': course_obj.id,
        'owners': course_obj.owners_ids,
        'titel': course_obj.title,
        'description': course_obj.description,
        'created_at': course_obj.created_at,
        'is_active': course_obj.is_active,
        'course_data': course_obj.course_data,
        'passing': course_obj.passing,
        'passed': course_obj.passed,
        'likes': course_obj.likes,
        'ico_url': course_obj.ico_url,
        'rating': course_obj.rating,
    }
