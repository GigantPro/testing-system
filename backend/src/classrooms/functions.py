from typing import Any
from sqlalchemy import select

from ..auth.database import User, Role
from .database import engine


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
