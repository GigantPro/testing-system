from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy

from ..config import db_config
from ..database import User
from .manager import get_user_manager

__all__ = (
    "cookie_transport",
    "get_jwt_strategy",
    "auth_backend",
    "fastapi_users",
)

cookie_transport = CookieTransport(
    cookie_name='auth_key',
    cookie_max_age=db_config.TTL_COOKIE_DAYS,
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=db_config.SECRET, lifetime_seconds=db_config.TTL_COOKIE_DAYS)


auth_backend = AuthenticationBackend(
    name='AuthBackend',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
