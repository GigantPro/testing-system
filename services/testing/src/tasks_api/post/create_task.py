from fastapi import Body

from src.types import CreateTaskModel, ReadTaskModel

from ..router import tasks_api

__all__ = ("task_create",)

@tasks_api.post('/create_task')
async def task_create(
    new_task: CreateTaskModel,
    secret: str = Body(...),
) -> ReadTaskModel:
    pass
