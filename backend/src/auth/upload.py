import base64
from random import randint
from datetime import datetime

from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

from .auth import fastapi_users
from ..config import config


current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

upload_router = APIRouter(prefix='/upload')


@upload_router.post('/avatar')
async def get_user_by_id(file_type: str = Form(...), filedata: str = Form(...)) -> str:
    filedata = filedata.strip()
    img_recovered = base64.b64decode(filedata)  # decode base64string
    file_name = f'avatar_' \
        f'{str(datetime.timestamp(datetime.now())).replace(".", "")}_{randint(10**10, 10**11 - 1)}.{file_type}'
    with open(f'{config.static_files_path}/' + file_name, 'wb') as file_write:
        file_write.write(img_recovered)
    return f'/api/static/{file_name}'
