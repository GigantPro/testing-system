from sqlalchemy import select

from src.database import User, engine

__all__ = ('get_user_by_id',)

async def get_user_by_id(user_id: int) -> None | User:
    async with engine.connect() as connection:
        user = await connection.execute(
            select(User) \
            .where(User.id == user_id)
        )
        return user.fetchone()
