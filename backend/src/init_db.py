from .auth.init_roles import init_roles
from .auth.database import create_db_and_tables as auth_db_create
from .classrooms.database import create_db_and_tables as classrooms_db_create
from .courses.database import create_db_and_tables as courses_db_create


async def init_db() -> None:
    await auth_db_create()
    await init_roles()

    await classrooms_db_create()
    await courses_db_create()
