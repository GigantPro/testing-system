from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .config import config


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
