from sqlalchemy import update

from src.database import User, engine


__all__ = (
    "__update_verification_status",
)

async def __update_verification_status(user_id: int) -> None:
    async with engine.connect() as connection:
        await connection.execute(
            update(User) \
            .where(User.id == user_id) \
            .values(is_verified=True)
        )
        await connection.commit()
