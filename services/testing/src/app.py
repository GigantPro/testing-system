from os import system

from fastapi import FastAPI
from loguru import logger

from .config import config
from .logger import init_logger
from .tasks_api import tasks_api

app = FastAPI(
    title='Testing.Edu.Xiver',
    debug=config.debug,
    openapi_url='/openapi.json',
    docs_url='/docs',
    root_path='/tests',
)

app.include_router(
    tasks_api,
)


@app.on_event('startup')
async def on_startup() -> None:
    await init_logger()
    system('alembic upgrade head')

    logger.info('App started')
