from sqlalchemy.inspection import inspect

from src.auth.schemas import UserRead
from src.database.models.user import User

__all__ = ("get_user_read_by_user",)

async def get_user_read_by_user(user: User) -> UserRead:
    userread_cfg = {}

    columns_user = list(inspect(User).c.keys())
    columns_user_read = list(UserRead.__fields__.keys())

    for id_ in range(len(columns_user)):
        if columns_user[id_] in columns_user_read:
            userread_cfg[columns_user[id_]] = user.__getattribute__(columns_user[id_])

    return UserRead(**userread_cfg)
