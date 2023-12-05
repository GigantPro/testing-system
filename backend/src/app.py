from os import makedirs

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger

from .auth import auth_backend, fastapi_users, user_get_router
from .auth.schemas import UserCreate, UserRead
from .classrooms import classrooms_router
from .config import config
from .courses import courses_router
from .database import async_session_maker
from .init_db import init_db
from .logger import init_logger
from .tgbot import bot, send_notify, start_bot

bot_turn = []

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
async def on_startup() -> None:
    await init_db()
    await init_logger()

    if config.tg_bot_token:
        logger.info('Find tg bot token. Start bot')
        bot_turn.append(await start_bot())

    else:
        logger.warning('Not find tg bot token. Skip bot')

    logger.info('App started')


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await async_session_maker.begin().async_session.close_all()
    await bot.close()
    logger.info('App shut down')


@app.exception_handler(500)
async def internal_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    error_message = f'Internal server error: {request.url} | {request.method} | {request.headers} | {exc}'
    logger.error(error_message)

    await send_notify(request, exc)

    return JSONResponse(status_code=500, content=jsonable_encoder({"code": 500, "msg": "Internal Server Error"}))
