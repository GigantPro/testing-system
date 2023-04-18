from fastapi import FastAPI

from .init_db import init_db
from .auth.database import async_session_maker
from .auth.schemas import UserCreate, UserRead
from .auth.auth import auth_backend, fastapi_users
from .config import config
from .classrooms.router import classrooms_router


app = FastAPI(
    title='Edu.Xiver',
    debug=config.debug,
    openapi_url='/openapi.json',
    docs_url='/docs',
    root_path='/api',
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth',
    tags=['auth'],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)

app.include_router(
    classrooms_router,
    tags=['classrooms']
)

@app.on_event('startup')
async def on_startup():
    await init_db()


@app.on_event('shutdown')
async def on_shutdown():
    await async_session_maker.begin().async_session.close_all()
