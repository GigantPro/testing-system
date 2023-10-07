from datetime import datetime

from pydantic import BaseModel


__all__ = (
    "ClassInviteModel",
)

class ClassInviteModel(BaseModel):
    id: int
    invite_code: str
    created_at: int
    created_at: datetime
    works_end: datetime
    is_active: bool
    creator_id: int
    invites_last: int
