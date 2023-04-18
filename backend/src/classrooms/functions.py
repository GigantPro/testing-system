from typing import Any
from sqlalchemy import select, insert
from sqlalchemy.inspection import inspect
from string import ascii_lowercase, ascii_uppercase
import random
from datetime import datetime, timedelta

from ..auth.database import User, Role
from .database import engine, ClassInvite, Classroom


async def has_permission(user: User, permission: str) -> Any | None:
    """Checks if the user has permission

    Args:
        user (User): User object
        permission (str): Permission name

    Returns:
        Any | None: Returns None if there is no permission, if it is, then its value
    """
    async with engine.connect() as connection:
        role = await connection.execute(select(Role)\
            .where(Role.id == user.role_id))
        role_perms = role.fetchone()[-1]
        return role_perms.get(permission, None) if role_perms else None


async def generate_invite_class_chars() -> str:
    """Fenerate unique charset with len=10

    Returns:
        str: unique generated charset
    """
    async with engine.connect() as connection:
        while True:
            generated_code = ''.join(
                [random.choice(ascii_lowercase + ascii_uppercase + '0123456789') for _ in range(10)]
            )
            data = await connection.execute(select(ClassInvite).where(ClassInvite.invite_code == generated_code))
            data = data.fetchone()
            if not data:
                return generated_code

async def save_generated_class(user: User, generated_code: str, class_name: str) -> None:
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
        res = max([i[0] for i in res])

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
