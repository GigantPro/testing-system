import json

from fastapi import APIRouter, Depends

from ..database import User
from .funcstions import (
    _get_user_read_by_user,
)
from const import current_active_user

self_router = APIRouter(prefix='/self')


@self_router.get('/who_am_i')
async def who_am_i(user: User = Depends(current_active_user)) -> dict:
    user_read = await _get_user_read_by_user(user)
    return json.loads(user_read.json())
