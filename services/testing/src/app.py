import asyncio
from os import system

from fastapi import FastAPI
from loguru import logger

from .config import config
from .logger import init_logger
from .task_manager import TaskManager
from .tasks_api import tasks_api_router

task_manager = TaskManager()

app = FastAPI(
    title='Testing.Edu.Xiver',
    debug=config.debug,
    openapi_url='/openapi.json',
    docs_url='/docs',
    # root_path='/tests',
)

app.include_router(
    tasks_api_router,
)


@app.on_event('startup')
async def on_startup() -> None:
    await init_logger()
    system('alembic upgrade head')

    asyncio.run_coroutine_threadsafe(task_manager.start(), asyncio.get_event_loop())

    logger.info('App started')


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await task_manager.stop()

    logger.info('App stopped')
