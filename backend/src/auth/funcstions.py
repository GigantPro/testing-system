from sqlalchemy import select
from sqlalchemy.inspection import inspect

from .database import User, engine
from .schemas import UserRead


async def _get_user_by_id(user_id: int) -> None | User:
    async with engine.connect() as connection:
        user = await connection.execute(
            select(User) \
            .where(User.id == user_id)
        )
        user = user.fetchone()
    
        if not user:
            return None

        user_cfg = {}
        columns = inspect(User).c.keys()

        for i in range(len(columns)):
            user_cfg[columns[i]] = user[i]

        return User(**user_cfg)

async def _get_user_read_by_user(user: User) -> UserRead:
    userread_cfg = {}

    columns_user = list(inspect(User).c.keys())
    columns_user_read = list(UserRead.__fields__.keys())

    for id_ in range(len(columns_user)):
        if columns_user[id_] in columns_user_read:
            userread_cfg[columns_user[id_]] = user.__getattribute__(columns_user[id_])

    return UserRead(**userread_cfg)
