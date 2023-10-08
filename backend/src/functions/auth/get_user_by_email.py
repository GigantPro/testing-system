from sqlalchemy import select

from src.database import User, engine


__all__ = ("get_user_by_email",)

async def get_user_by_email(email: str) -> None | User:
    async with engine.connect() as connection:
        user = await connection.execute(
            select(User) \
            .where(User.email == email)
        )
        return user.fetchone()