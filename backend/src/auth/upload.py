import json
from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse

from .auth import fastapi_users


current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

upload_router = APIRouter(prefix='/upload')


@upload_router.post('/avatar')
async def get_user_by_id(file: UploadFile) -> str:
    print(file.size)
    return '123'
