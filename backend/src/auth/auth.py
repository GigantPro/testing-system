from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import AuthenticationBackend, JWTStrategy

from .manager import get_user_manager
from ..database import User
from ..db_config import config


cookie_transport = CookieTransport(
    cookie_name='auth_key',
    cookie_max_age=config.TTL_COOKIE_DAYS,
)

SECRET = config.SECRET


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=config.TTL_COOKIE_DAYS)


auth_backend = AuthenticationBackend(
    name='AuthBackend',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
