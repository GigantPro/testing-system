from fastapi import Depends
from fastapi.responses import JSONResponse

from src.database import User
from src.functions import (
    check_for_valid_invite,
    activate_invite,
)
from src.const import current_active_user
from ..router import classrooms_router



@classrooms_router.get('/join/{invite_code}')
async def join_class_room(invite_code: str, user: User = Depends(current_active_user)) -> dict:
    if not check_for_valid_invite(invite_code):
        return JSONResponse(content={'message': 'Invite code does not exist'}, status_code=404)

    res = await activate_invite(user, invite_code)
    return res