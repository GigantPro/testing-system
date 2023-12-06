from fastapi import Depends
from fastapi.responses import JSONResponse
from loguru import logger

from src.const import current_active_user
from src.database import User
from src.functions import (
    activate_invite,
    check_for_valid_invite,
)

from ..router import classrooms_router


@classrooms_router.get('/join/{invite_code}')
async def join_class_room(invite_code: str, user: User = Depends(current_active_user)) -> dict:
    logger.info(f"Join class room: {invite_code} from {user.id}")
    if not check_for_valid_invite(invite_code):
        logger.info(f"Invite code does not exist: {invite_code} from {user.id}")
        return JSONResponse(content={'message': 'Invite code does not exist'}, status_code=404)

    res = await activate_invite(user, invite_code)
    return res
