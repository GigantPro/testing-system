from datetime import datetime

from pydantic import BaseModel, Field, validator

from src.auth.standart_roles import standart_roles


__all__ = (
    "UserReadModel",
)

class UserReadModel(BaseModel):
    class Config:
        orm_mode = True

    id: int
    username: str
    registered_at: datetime
    changed_time: datetime
    role: str = Field(alias="role_id")
    name: str
    surname: str
    ico_url: str
    
    @validator("role")
    def validate_role(cls, value):  # noqa: N805
        value = int(value)
        return [i for i in standart_roles if i['id'] == value][0]['name']
