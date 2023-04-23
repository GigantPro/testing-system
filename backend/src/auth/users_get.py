import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .auth import fastapi_users
from .funcstions import (
    _get_user_by_id,
    _get_user_read_by_user,
)
from ..verification.verification import verification_router


current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

user_get_router = APIRouter(prefix='/user')

user_get_router.include_router(
    verification_router
)


@user_get_router.get('/{user_id}')
async def get_user_by_id(user_id: int) -> dict:
    user = await _get_user_by_id(user_id)

    if not user:
        return JSONResponse({'message': 'User not found'}, status_code=404)

    user_read = await _get_user_read_by_user(user)
    return json.loads(user_read.json())


@user_get_router.get('/{user_id}/email')
async def get_user_user_by_id(user_id: int) -> str:
    user = await _get_user_by_id(user_id)

    if not user:
        return JSONResponse('User not found', status_code=404)

    return user.email
