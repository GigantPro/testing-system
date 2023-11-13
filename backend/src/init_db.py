from os import system

from .auth.init_roles import init_roles


__all__ = ("init_db",)

async def init_db() -> None:
    system('alembic upgrade head')
    await init_roles()
