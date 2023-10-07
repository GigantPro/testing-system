from sqlalchemy import select

from src.database import Course, engine


__all__ = ("get_course_by_id",)

async def get_course_by_id(course_id: int) -> Course:
    async with engine.connect() as connection:
        db_answer = await connection.execute(select(Course).where(Course.id == course_id))
        return db_answer.fetchone()
