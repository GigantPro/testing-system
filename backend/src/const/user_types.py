from ..auth.auth import fastapi_users

__all__ = (
    'current_user',
    'current_superuser',
    'current_active_user',
    'current_active_verified_user',
)

current_user        = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_superuser   = fastapi_users.current_user(active=True, superuser=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
