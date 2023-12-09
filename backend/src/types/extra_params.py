
from pydantic import BaseModel, Field

__all__ = (
    "ExtraParamsModel",
)

class ExtraParamsModel(BaseModel):
    class Config:
        from_attributes = True
        from_orm = True

    time_limit: int = Field(5, nullable=False)
    """Secconds"""
    memory_limit: int = Field(128, nullable=False)
    """Megabytes"""
    cpu_limit: float = Field(.5, nullable=False)
