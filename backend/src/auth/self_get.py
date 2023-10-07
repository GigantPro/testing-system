import json

from fastapi import APIRouter, Depends

from ..database import User
from src.functions import get_user_read_by_user
from src.const import current_active_user

__all__ = (
    "self_router",
    "who_am_i",
)

self_router = APIRouter(prefix='/self')


@self_router.get('/who_am_i')
async def who_am_i(user: User = Depends(current_active_user)) -> dict:
    user_read = await get_user_read_by_user(user)
    return json.loads(user_read.json())
