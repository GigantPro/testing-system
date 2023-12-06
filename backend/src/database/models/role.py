from sqlalchemy import JSON, Column, Integer, String

from ..base import Base

__all__ = ("Role",)

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)
