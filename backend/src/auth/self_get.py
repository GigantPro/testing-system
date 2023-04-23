import json

from fastapi import APIRouter, Depends

from .database import User
from .auth import fastapi_users
from .funcstions import (
    _get_user_read_by_user,
)


current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

self_router = APIRouter(prefix='/self')


@self_router.get('/who_am_i')
async def who_am_i(user: User = Depends(current_active_user)) -> dict:
    user_read = await _get_user_read_by_user(user)
    return json.loads(user_read.json())
