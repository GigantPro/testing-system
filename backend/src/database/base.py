from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from ..config import db_config

__all__ = (
    "engine",
    "async_session_maker",
    "get_async_session",
)

DATABASE_URL = f'postgresql+asyncpg://{db_config.POSTGRES_USER}:{db_config.POSTGRES_PASSWORD}@'\
    f'{db_config.DB_HOST}:{db_config.DB_PORT}/{db_config.POSTGRES_DB}'

class Base(DeclarativeBase):
    pass

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
