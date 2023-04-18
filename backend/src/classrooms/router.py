from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ..auth.database import User
from ..auth.auth import fastapi_users
from .functions import has_permission


current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

classrooms_router = APIRouter(prefix='/classrooms')


@classrooms_router.post('/create')
async def create_class_room(user: User = Depends(current_active_user)) -> dict:
    perm = await has_permission(user, 'create_classrooms')
    if not perm:
        return JSONResponse(content={"message": "Permission Denied"}, status_code=403)

    return {'status': 'success'}


@classrooms_router.get('/join/{invite_code}')
async def join_class_room(join_link_id: str, user: User = Depends(current_active_user)) -> dict:
    ...
