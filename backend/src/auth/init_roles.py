from sqlalchemy import select, insert, update

from ..database import engine, Role
from .standart_roles import standart_roles


__all__ = ("init_roles",)


async def init_roles() -> None:
    async with engine.connect() as connection:
        for role_ in standart_roles:
            result = await connection.execute(select(Role).where(Role.id == role_['id']))
            if not result.fetchone():
                await connection.execute(insert(Role).values(**role_))
            else:
                await connection.execute(update(Role).where(Role.id == role_['id']).values(**role_))

        await connection.commit()
