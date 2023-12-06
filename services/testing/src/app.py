from fastapi import FastAPI
from fastapi.responses import JSONResponse
from loguru import logger

from .config import config
from .logger import init_logger

app = FastAPI(
    title='Testing.Edu.Xiver',
    debug=config.debug,
    openapi_url='/openapi.json',
    docs_url='/docs',
    root_path='/tests',
)

@app.get('/test')
async def course_by_id() -> JSONResponse:
    return JSONResponse(status_code=200, content={"code": 200, "msg": "OK"})


@app.on_event('startup')
async def on_startup() -> None:
    await init_logger()

    logger.info('App started')
