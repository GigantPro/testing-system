from fastapi.responses import JSONResponse

from ..schemas import UserRead
from ..router import user_get_router
from src.functions import get_user_read_by_user, get_user_by_id


__all__ = ("user_by_id",)

@user_get_router.get('/{user_id}')
async def user_by_id(user_id: int) -> UserRead:
    user = await get_user_by_id(user_id)

    if not user:
        return JSONResponse({'message': 'User not found'}, status_code=404)

    user_read = await get_user_read_by_user(user)
    return user_read
