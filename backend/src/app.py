from fastapi import FastAPI
import fastapi_users

from .auth.init_roles import init_roles
from .auth.manager import get_user_manager
from .auth.database import User, create_db_and_tables, async_session_maker
from .auth.schemas import UserCreate, UserRead
from .auth.auth import auth_backend
from .config import config


app = FastAPI(
    title="Edu.Xiver",
    debug=config.debug,
    openapi_url="/openapi.json",
    docs_url="/docs",
    root_path='/api',
)

fastapi_users = fastapi_users.FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
    await init_roles()


@app.on_event("shutdown")
async def on_shutdown():
    await async_session_maker.begin().async_session.close_all()
