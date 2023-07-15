from datetime import datetime
from typing import AsyncGenerator

from sqlalchemy import JSON, TIMESTAMP, Column, Integer, Boolean, String, FLOAT
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from ..db_config import config


DATABASE_URL = f'postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@'\
    f'{config.DB_HOST}:{config.DB_PORT}/{config.POSTGRES_DB}'


class Base(DeclarativeBase):
    pass


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    teachers_ids = Column(JSON, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    ico_url = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    passing_id = Column(JSON, default=[])
    passed_id = Column(JSON, default=[])
    reviews = Column(JSON, default=[])
    rating = Column(FLOAT, default=.0)
    course_data = Column(JSON, default={})

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
