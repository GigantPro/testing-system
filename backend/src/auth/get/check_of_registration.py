from src.functions import get_user_by_username, get_user_by_email
from ..router import user_get_router


__all__ = ("check_of_registration",)

@user_get_router.get('/check', description='Return True if username / email is busy.')
async def check_of_registration(username: str, email: str):
    user_by_username = await get_user_by_username(username)
    user_by_email = await get_user_by_email(email)

    return {
        'username': True if user_by_username else False,
        'email': True if user_by_email else False,
    }