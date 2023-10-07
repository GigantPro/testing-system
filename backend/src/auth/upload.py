import base64
from random import randint
from datetime import datetime

from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

from ..config import config


__all__ = (
    "upload_router",
    "get_user_by_id",
)

upload_router = APIRouter(prefix='/upload')

@upload_router.post('/avatar')
async def get_user_by_id(file_type: str = Form(...), filedata: str = Form(...)) -> str:
    if file_type not in ['png', 'jpeg']:
        return JSONResponse({'message': 'Incorrect file format.'}, 400)

    filedata = filedata.strip()
    img_recovered = base64.b64decode(filedata)  # decode base64string
    file_name = f'avatar_' \
        f'{str(datetime.timestamp(datetime.now())).replace(".", "")}_{randint(10**10, 10**11 - 1)}.{file_type}'
    with open(f'{config.static_files_path}/' + file_name, 'wb') as file_write:
        file_write.write(img_recovered)
    return f'/api/static/{file_name}'
