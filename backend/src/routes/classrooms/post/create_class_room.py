from fastapi import Depends, Request
from fastapi.responses import JSONResponse
from loguru import logger

from src.auth import current_active_user
from src.database import User
from src.functions import (
    generate_invite_class_chars,
    has_permission,
    save_generated_class,
)

from ..router import classrooms_router

__all__ = (
    "create_class_room",
)

@classrooms_router.post('/create')
async def create_class_room(class_name: str, request: Request, user: User = Depends(current_active_user)) -> dict:
    perm = await has_permission(user, 'create_classrooms')
    logger.info(f"Create new class room: {class_name} from {user.id} with {perm=}")
    if not perm:
        return JSONResponse(content={'message': 'Permission Denied'}, status_code=403)

    generated_code_link = await generate_invite_class_chars()
    await save_generated_class(user, generated_code_link, class_name)

    return {
        'message': 'success',
        'url': '/'.join(str(request.url).split('/')[:-2]) + '/join/' + generated_code_link
    }
