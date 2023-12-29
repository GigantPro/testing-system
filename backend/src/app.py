from os import makedirs

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger

from .auth import auth_backend, fastapi_users, user_get_router
from .auth.schemas import UserCreate, UserRead
from .config import config
from .database import async_session_maker
from .functions import send_error_msg
from .init_db import init_db
from .logger import init_logger
from .routes import classrooms_router, courses_router, solution_router
from .solutions_engine import solutions_engine

bot_turn = []

app = FastAPI(
    title='Edu.Xiver',
    debug=config.debug,
    openapi_url='/openapi.json',
    docs_url='/docs',
    root_path='/api',
)

makedirs(config.static_files_path, exist_ok=True)
makedirs(config.solutions_files_path, exist_ok=True)
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

app.include_router(
    solution_router,
    tags=['solutions']
)

@app.on_event('startup')
async def on_startup() -> None:
    await init_logger()
    await init_db()
    
    await solutions_engine.start()

    logger.info('App started')


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await async_session_maker.begin().async_session.close_all()

    await solutions_engine.stop()
    logger.info('App shut down')


@app.exception_handler(500)
async def internal_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    error_message = f'Internal server error: {request.url} | {request.method} | {request.headers} | {exc}'
    logger.error(error_message)

    await send_error_msg(exc, request, 500)

    return JSONResponse(status_code=500, content=jsonable_encoder({"code": 500, "msg": "Internal Server Error"}))
