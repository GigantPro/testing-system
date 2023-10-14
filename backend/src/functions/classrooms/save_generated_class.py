from datetime import datetime, timedelta

from sqlalchemy import insert, select

from src.database import engine, User, Classroom, ClassInvite


__all__ = ("save_generated_class",)

async def save_generated_class(user: User, generated_code: str, class_name: str) -> None:
    """Save class by generation code

    Args:
        user (User): creator user object
        generated_code (str): Code for invite link
        class_name (str): Name of class
    """
    async with engine.connect() as connection:
        await connection.execute(
            insert(Classroom)\
            .values(
                class_name=class_name,
                owner_id=user.id,
                admins=[user.id],
                members=[user.id],
            )
        )
        res = await connection.execute(select(Classroom).column(Classroom.id))
        res = res.fetchall()
        res = max(res, key=lambda i: i[0])

        await connection.execute(
            insert(ClassInvite)\
            .values(
                invite_code = generated_code,
                class_id = res,
                works_end = datetime.now() + timedelta(days=30),
                creator_id = user.id,
            )
        )
        await connection.commit()
