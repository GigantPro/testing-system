from .router import classrooms_router
from .database import engine


@classrooms_router.post('/create')
async def create_class_room() -> dict:
    ...