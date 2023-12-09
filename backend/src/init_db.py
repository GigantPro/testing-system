from os import system

from loguru import logger

from .auth.init_roles import init_roles

__all__ = ("init_db",)

async def init_db() -> None:
    logger.info('Starting DB Initialization')
    system('alembic upgrade head')
    await init_roles()
    logger.info('DB is initialized')
