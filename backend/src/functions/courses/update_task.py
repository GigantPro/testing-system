from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from src.database import Course, Module, Task, User
from src.types import ReadTaskModel, UpdateTaskModel


async def update_task(
    updated_task: UpdateTaskModel, task_id: int, user: User, session: AsyncSession
) -> ReadTaskModel:
    try:
        task = (await session.scalars(select(Task).where(Task.id == task_id))).one()
    except NoResultFound:
        return JSONResponse(status_code=404, content={'message': 'Task not found'})

    try:
        module = (await session.scalars(select(Module).where(Module.id == task.module_id))).one()
    except NoResultFound:
        return JSONResponse(status_code=404, content={'message': 'Module not found'})

    try:
        course = (await session.scalars(select(Course).where(Course.id == module.course_id))).one()
    except NoResultFound:
        return JSONResponse(status_code=404, content={'message': 'Course not found'})

    if user.id not in course.teachers_ids and user.role_id < 4:
        return JSONResponse(status_code=403, content={'message': 'Forbidden'})

    for key, value in updated_task.dict().items():
        if value:
            setattr(task, key, value)

    await session.commit()
    await session.refresh(task)

    return ReadTaskModel(**task.__dict__)
