from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from ..config import config



__all__ = ("Base", "Session", "session", "engine")

engine = create_engine(f'postgresql://{config.pg_user}:{config.pg_password}@{config.pg_ip}:{config.pg_port}/{config.pg_base}')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
