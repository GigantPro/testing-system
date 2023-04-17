from datetime import datetime
from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy import JSON, TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from ..db_config import config
from ..models.models import user



DATABASE_URL = f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@"\
    f"{config.DB_HOST}:{config.DB_PORT}/{config.POSTGRES_DB}"


class Base(DeclarativeBase):
    pass


class Classroom(Base):
    __tablename__ = 'classroom'

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey(user.c.id))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    admins = Column(JSON, nullable=False)
    members = Column(JSON, nullable=False)
    optins = Column(JSON)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
