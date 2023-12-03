from typing import Any

from sqlalchemy import select

from src.database import Course, engine
from src.types import CourseFullModel

__all__ = ("get_course_by_param",)

async def get_course_by_param(param: str, value: Any) -> CourseFullModel | None:  # noqa: ANN401
    if param == 'id':
        value = int(value)

    async with engine.connect() as connection:
        db_answer = await connection.execute(select(Course).where(Course.__dict__[param] == value))

    answer = db_answer.fetchone()
    if answer:
        return CourseFullModel.from_orm(answer)
    return None
