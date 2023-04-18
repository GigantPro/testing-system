from datetime import datetime
from typing import AsyncGenerator

from sqlalchemy import JSON, TIMESTAMP, DateTime, Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

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


class ClassInvite(Base):
    __tablename__ = 'classinvite'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    invite_code = Column(String, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    class_id = Column(Integer, ForeignKey(Classroom.id), nullable=False)
    works_end = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    creator_id = Column(Integer, ForeignKey(user.c.id), nullable=False)
    invites_last = Column(Integer, default=1000000, nullable=False)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
