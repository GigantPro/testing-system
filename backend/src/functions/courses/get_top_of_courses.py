from sqlalchemy import select
from sqlalchemy.sql.expression import func

from src.database import engine, Course, json_array_length


__all__ = ("get_top_of_courses",)

async def get_top_of_courses(count: int) -> list[Course]:
    async with engine.connect() as connection:
        db_answer = await connection.execute(
            select(Course)
            .where(Course.is_active == True)
            .order_by(func.json_array_length(Course.passed_id), Course.rating, \
                json_array_length(Course.reviews), json_array_length(Course.passing_id))
            .limit(count)
        )
        return db_answer.fetchall()
