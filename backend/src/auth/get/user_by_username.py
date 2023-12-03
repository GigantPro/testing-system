from fastapi.responses import JSONResponse

from src.functions import get_user_by_username, get_user_read_by_user

from ..router import user_get_router
from ..schemas import UserRead

__all__ = ("user_by_username",)

@user_get_router.get('/username/{username}')
async def user_by_username(username: str) -> UserRead:
    user = await get_user_by_username(username)

    if not user:
        return JSONResponse('User not found', status_code=404)

    return await get_user_read_by_user(user)
