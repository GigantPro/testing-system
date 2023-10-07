from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import AuthenticationBackend, JWTStrategy

from .manager import get_user_manager
from ..database import User
from ..config import db_config


cookie_transport = CookieTransport(
    cookie_name='auth_key',
    cookie_max_age=db_config.TTL_COOKIE_DAYS,
)

SECRET = db_config.SECRET


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=db_config.TTL_COOKIE_DAYS)


auth_backend = AuthenticationBackend(
    name='AuthBackend',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
