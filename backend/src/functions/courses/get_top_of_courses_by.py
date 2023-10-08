from typing import Any

from sqlalchemy import select

from src.database import engine, Course


__all__ = ("get_top_of_courses_by",)

async def get_top_of_courses_by(start_index: int, count: int, by_: Any) -> list[Course]:
    """Return sorted courses by param

    Args:
        start_index (int): OFFSET param
        count (int): count of returned params
        by_ (Any): param like Course.id, Course.name and etc

    Returns:
        list[Course]: result of database fetch
    """
    async with engine.connect() as connection:
        db_answer = await connection.execute(
            select(Course)
            .where(Course.is_active == True)
            .order_by(by_)
            .limit(count)
            .offset(start_index)
        )
        return db_answer.fetchall()
