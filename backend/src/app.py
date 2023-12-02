from os import makedirs

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .init_db import init_db
from .database import async_session_maker
from .auth.schemas import UserCreate, UserRead
from .auth import user_get_router
from .auth import auth_backend, fastapi_users
from .config import config
from .classrooms import classrooms_router
from .courses import courses_router


app = FastAPI(
    title='Edu.Xiver',
    debug=config.debug,
    openapi_url='/openapi.json',
    docs_url='/docs',
    root_path='/api',
)

makedirs(config.static_files_path, exist_ok=True)
app.mount("/static", StaticFiles(directory=config.static_files_path))

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

app.include_router(
    user_get_router,
    tags=['users']
)

app.include_router(
    courses_router,
    tags=['courses']
)

@app.on_event('startup')
async def on_startup():
    await init_db()


@app.on_event('shutdown')
async def on_shutdown():
    ...
