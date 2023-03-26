from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy.access_token import \
        SQLAlchemyBaseAccessTokenTable
from sqlalchemy import Column, ForeignKey, Integer, String, JSON, TIMESTAMP, \
        Boolean
from sqlalchemy.sql import func, text

from sqlalchemy.ext.declarative import declarative_base

from .engine import Base

FakeBase = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    login = Column(String(255), nullable=False)
    email = Column(String(length=320), unique=True, index=True,
                   nullable=False)
    hashed_password = Column(String(length=1024),
                             nullable=False)
    settings = Column(JSON, server_default=text("'{}'::json"), nullable=False)
    avatar_file_path = Column(String(255), nullable=True)
    registered_at = Column(TIMESTAMP(timezone=True),
                           server_default=func.now(),
                           nullable=False)
    admin_level = Column(Integer, server_default=0,
                          nullable=False)
    is_active = Column(Boolean, server_default='true',
                       nullable=False)
    is_verified = Column(Boolean, server_default='false',
                         nullable=False)


class AccessToken(SQLAlchemyBaseAccessTokenTable[int], Base):
    token = Column(String(length=43), primary_key=True)
    created_at = Column(
        TIMESTAMP(timezone=True),
        index=True,
        nullable=False,
        server_default=func.now())

    user_id = Column(Integer,
                     ForeignKey("users.id", ondelete="cascade"),
                     nullable=False)
