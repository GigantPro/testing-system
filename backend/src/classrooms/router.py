from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from ..database import User
from src.functions import (
    has_permission,
    generate_invite_class_chars,
    save_generated_class,
    check_for_valid_invite,
    activate_invite,
)
from src.const import current_active_user


__all__ = (
    "classrooms_router",
    "create_class_room",
    "join_class_room"
)

classrooms_router = APIRouter(prefix='/classroom')


@classrooms_router.post('/create')
async def create_class_room(class_name: str, request: Request, user: User = Depends(current_active_user)) -> dict:
    perm = await has_permission(user, 'create_classrooms')
    if not perm:
        return JSONResponse(content={'message': 'Permission Denied'}, status_code=403)

    generated_code_link = await generate_invite_class_chars()
    await save_generated_class(user, generated_code_link, class_name)

    return {
        'message': 'success',
        'url': '/'.join(str(request.url).split('/')[:-2]) + '/join/' + generated_code_link
    }


@classrooms_router.get('/join/{invite_code}')
async def join_class_room(invite_code: str, user: User = Depends(current_active_user)) -> dict:
    if not check_for_valid_invite(invite_code):
        return JSONResponse(content={'message': 'Invite code does not exist'}, status_code=404)

    res = await activate_invite(user, invite_code)
    return res
