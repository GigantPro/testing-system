from sqlalchemy import Column, Integer, String, JSON

from ..base import Base


__all__ = ("Role",)

class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)
