from fastapi import Depends

from src.const import current_active_user
from src.database import User
from src.functions import get_user_read_by_user

from ..router import self_router
from ..schemas import UserRead

__all__ = (
    "who_am_i",
)

@self_router.get('/who_am_i')
async def who_am_i(user: User = Depends(current_active_user)) -> UserRead:
    user_read = await get_user_read_by_user(user)
    return user_read
