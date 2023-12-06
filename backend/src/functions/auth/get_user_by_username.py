from sqlalchemy import select

from src.database import User, engine

__all__ = ("get_user_by_username",)

async def get_user_by_username(username: str) -> None | User:
    async with engine.connect() as connection:
        user = await connection.execute(
            select(User) \
            .where(User.username == username)
        )
        return user.fetchone()
