from typing import Any

from fastapi import Depends, Form
from fastapi.responses import JSONResponse

from ..router import courses_router
from database import User
from user_types import current_active_verified_user
from ..functions import create_new_course


@courses_router.post('/create')
async def create_course(
    title: str = Form(),
    description: str = Form(),
    user: User = Depends(current_active_verified_user),
) -> Any:
    await create_new_course(title, description, user)
    return JSONResponse({'message': 'success'}, 200)