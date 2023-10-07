from .auth.init_roles import init_roles
from .database import create_db_and_tables


async def init_db() -> None:
    await create_db_and_tables()
    await init_roles()
