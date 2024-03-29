from fastapi import Depends
from loguru import logger

from src.database import User
from src.functions import get_user_read_by_user

from ..router import self_router
from ..schemas import UserRead
from ..user_types import current_active_user

__all__ = (
    "who_am_i",
)

@self_router.get('/who_am_i')
async def who_am_i(user: User = Depends(current_active_user)) -> UserRead:
    logger.info(f"Get who am i: {user.id}")
    user_read = await get_user_read_by_user(user)
    return user_read
