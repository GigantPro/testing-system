from .router import *
from .verification import *
from .get import *
from .post import *
from .auth import *
from .init_roles import *
from .manager import *
from .schemas import *


user_get_router.include_router(
    upload_router,
)

user_get_router.include_router(
    verification_router,
)
user_get_router.include_router(
    self_router,
)

