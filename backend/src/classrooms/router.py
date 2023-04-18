from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from ..auth.database import User
from ..auth.auth import fastapi_users
from .functions import has_permission, generate_invite_class_chars, save_generated_class


current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

classrooms_router = APIRouter(prefix='/classrooms')


@classrooms_router.post('/create')
async def create_class_room(class_name: str, request: Request, user: User = Depends(current_active_user)) -> dict:
    perm = await has_permission(user, 'create_classrooms')
    if not perm:
        return JSONResponse(content={"message": "Permission Denied"}, status_code=403)

    generated_code_link = await generate_invite_class_chars()
    await save_generated_class(user, generated_code_link, class_name)

    return {'url': '/'.join(str(request.url).split('/')[:-2]) + '/join/' + generated_code_link}


@classrooms_router.get('/join/{invite_code}')
async def join_class_room(join_link_id: str, user: User = Depends(current_active_user)) -> dict:
    ...
