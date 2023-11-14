from sqlalchemy import insert

from src.database import engine, User, Course
from src.types import FullModuleModel


__all__ = ("create_new_course",)

async def create_new_module(course_id: int, description: str, user: User) -> int | None:
    async with engine.connect() as connection:
        await connection.execute(
            insert(Course)
            .values(
                teachers_ids = [user.id],
                title = title,
                description = description,
            )
        )
        await connection.commit()

        # Fix me: Добавить возвращение присвоенного id
