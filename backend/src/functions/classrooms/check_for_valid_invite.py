from datetime import datetime

from sqlalchemy import select, update

from src.database import engine, ClassInvite


__all__ = ("check_for_valid_invite",)

async def check_for_valid_invite(invite_code: str) -> bool:
    async with engine.connect() as connection:
        res = await connection.execute(
            select(ClassInvite) \
            .where(ClassInvite.invite_code == invite_code)
        )
        res = res.fetchone()

        if not res:
            return False

        if res[5] is False or \
            res[8] == 0:
            return False
        if res[4] < datetime.now():
            await connection.execute(
                update(ClassInvite.is_active) \
                .where(ClassInvite.id == res[0]) \
                .values(False)
            )
            await connection.commit()
            return False
        return True
