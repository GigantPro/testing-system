from fastapi.responses import JSONResponse
from sqlalchemy import select, update

from src.database import ClassInvite, Classroom, User, engine

__all__ = ("activate_invite",)

async def activate_invite(user: User, invite_code: str) -> dict:
    async with engine.connect() as connection:
        invite_info = await connection.execute(
            select(ClassInvite) \
            .where(ClassInvite.invite_code == invite_code)
        )
        invite_info = invite_info.fetchone()

        class_room_info = await connection.execute(
            select(Classroom) \
            .where(Classroom.id == invite_info[3])
        )
        class_room_info = list(class_room_info.fetchone())

        if user.id in class_room_info:
            return JSONResponse(
                content={
                    'message': 'You are already in this class'
                },
                status_code=412,
            )

        await connection.execute(
            update(Classroom) \
            .where(Classroom.id == class_room_info[0]) \
            .values(members = class_room_info[5] + [user.id])
        )
        await connection.execute(
            update(ClassInvite) \
            .where(ClassInvite.id == invite_info[0]) \
            .values(invites_last = invite_info[7] - 1)
        )
        await connection.commit()
        return {
            'message': 'success'
        }
