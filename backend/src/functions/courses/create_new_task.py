from fastapi.responses import JSONResponse
from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Course, Module, Task, User
from src.types import CreateTaskModel, ReadTaskModel

__all__ = ("create_new_task",)


async def create_new_task(
    new_task: CreateTaskModel, module_id: int, course_id: int, user: User,
    session: AsyncSession,
) -> ReadTaskModel:
    session.begin()

    course = (await session.scalars(select(Course).where(Course.id == course_id))).one()

    if not course:
        return JSONResponse(status_code=404, content={"message": "Course not found"})

    if user.id not in course.teachers_ids and user.role_id < 4:
        return JSONResponse(status_code=403, content={"message": "Forbidden"})

    module = (await session.scalars(select(Module).where(Module.id == module_id))).one()

    if not module:
        return JSONResponse(status_code=404, content={"message": "Module not found"})

    task = Task(**new_task.dict(), course_id=course.id, module_id=module.id)

    session.add(task)

    await session.commit()
    await session.refresh(task)

    return ReadTaskModel.from_orm(task)
