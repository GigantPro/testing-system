from sqlalchemy import select
from sqlalchemy.sql.expression import func

from src.database import Course, engine, json_array_length

__all__ = ("get_top_of_courses",)

async def get_top_of_courses(start_index: int, count: int) -> list[Course]:
    async with engine.connect() as connection:
        db_answer = await connection.execute(
            select(Course)
            .where(Course.is_active is True)
            .order_by(func.json_array_length(Course.__table__.c.passed_id).desc(), Course.__table__.c.rating.desc(), \
                json_array_length(Course.__table__.c.reviews).desc(),
                json_array_length(Course.__table__.c.passing_id).desc())
            .limit(count)
            .offset(start_index)
        )
        return db_answer.fetchall()
