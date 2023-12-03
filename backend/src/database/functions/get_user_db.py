from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from ..base import get_async_session
from ..models.user import User

__all__ = ("get_user_db",)

async def get_user_db(session: AsyncSession = Depends(get_async_session)) -> SQLAlchemyUserDatabase:
    yield SQLAlchemyUserDatabase(session, User)
