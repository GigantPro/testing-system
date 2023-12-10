# ruff: noqa: F403, F405

from .auth import *
from .get import *
from .init_roles import *
from .manager import *
from .post import *
from .router import *
from .schemas import *
from .verification import *
from .user_types import *

user_get_router.include_router(
    upload_router,
)

user_get_router.include_router(
    verification_router,
)
user_get_router.include_router(
    self_router,
)

