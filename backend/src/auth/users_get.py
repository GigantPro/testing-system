import json
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .schemas import UserRead

from src.functions import (
    get_user_by_id as _get_user_by_id,
    get_user_read_by_user as _get_user_read_by_user,
    get_user_by_username as _get_user_by_username,
    get_user_by_email as _get_user_by_email,
)
from ..verification.verification import verification_router
from .self_get import self_router
from .upload import upload_router


__all__ = (
    "get_user_by_id",
    "user_get_router",
    "get_check_of_registration",
    "get_user_user_by_username",
    "get_user_email_user_by_id",
)

user_get_router = APIRouter(prefix='/user')
user_get_router.include_router(upload_router)

user_get_router.include_router(
    verification_router
)
user_get_router.include_router(
    self_router
)


@user_get_router.get('/check', description='Return True if username / email is busy.')
async def get_check_of_registration(username: str, email: str):
    user_by_username = await _get_user_by_username(username)
    user_by_email = await _get_user_by_email(email)

    return {
        'username': True if user_by_username else False,
        'email': True if user_by_email else False,
    }

@user_get_router.get('/username/{username}')
async def get_user_user_by_username(username: str) -> UserRead:
    user = await _get_user_by_username(username)

    if not user:
        return JSONResponse('User not found', status_code=404)

    return await _get_user_read_by_user(user)

@user_get_router.get('/{user_id}')
async def get_user_by_id(user_id: int) -> dict:
    user = await _get_user_by_id(user_id)

    if not user:
        return JSONResponse({'message': 'User not found'}, status_code=404)

    user_read = await _get_user_read_by_user(user)
    return json.loads(user_read.json())
