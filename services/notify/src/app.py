from fastapi import FastAPI
from loguru import logger

from .bot import bot, start_bot
from .config import config
from .logger import init_logger

bot_running = None

app = FastAPI(
    title='Notify.Edu.Xiver',
    debug=config.debug,
    openapi_url='/openapi.json',
    docs_url='/docs',
    root_path='/notify',
)

@app.on_event('startup')
async def startup() -> None:
    global bot_running

    await init_logger()

    bot_running = await start_bot()

    logger.info('Application started')


@app.on_event('shutdown')
async def shutdown() -> None:
    if bot_running:
        await bot.close()

    logger.info('Application stopped')
