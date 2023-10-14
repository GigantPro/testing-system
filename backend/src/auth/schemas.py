from typing import Optional
from fastapi_users import schemas


__all__ = (
    "UserRead",
    "UserCreate",
    "UserUpdate",
)

class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    name: str
    surname: str
    ico_url: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    email: str
    username: str
    password: str
    name: str
    surname: str
    ico_url: Optional[str] = '/api/static/standart_ico.png'
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    email: Optional[str]
    role_id: Optional[str]
    username: Optional[str]
    name: Optional[str]
    surname: Optional[str]
    ico_url: Optional[str]
    hashed_password: Optional[str]

    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]
