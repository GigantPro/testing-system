from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ..extra_params import ExtraParamsModel

__all__ = (
    "ServiceTaskModel",
)

class ServiceTaskModel(BaseModel):
    class Config:
        from_attributes = True
        from_orm = True

    id: int
    user_id: int

    status: str

    url_code_for_run: Optional[str] = Field(None, nullable=True)
    s_code_for_run: Optional[str] = Field(None, nullable=True)
    code_languge: str

    correct_output: Optional[str] = Field(None, nullable=True)
    correct: Optional[str] = Field(None, nullable=True)
    incorrect_log: Optional[str] = Field(None, nullable=True)

    created_at: datetime
    updated_at: datetime

    priority: int

    extra_params: ExtraParamsModel
