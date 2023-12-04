from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Course
from src.database import User, Module, Task
from src.types import CreateTaskModel, ReadTaskModel, FullModuleModel

__all__ = ("create_new_task",)


async def create_new_task(
    new_task: CreateTaskModel, module_id: int, course_id: int, user: User,
    session: AsyncSession,
) -> ReadTaskModel:
    session.begin()
    print(f'{course_id=}')
    course = await session.execute(
        select(Course)
        .where(Course.id == course_id)
    )
    course = course.fetchone()

    if not course:
        return JSONResponse(status_code=404, content={"message": "Course not found"})

    course = course[0]

    if user.id not in course.teachers_ids and user.role_id < 4:
        return JSONResponse(status_code=403, content={"message": "Forbidden"})

    module = await session.execute(
        select(Module)
        .where(Module.id == module_id)
    )
    module = module.fetchone()

    if not module:
        return JSONResponse(status_code=404, content={"message": "Module not found"})

    module = module[0]

    task = Task(
        title=new_task.title,
        description=new_task.description,
        module_id=module_id,
        type=new_task.type,
        text=new_task.text,
        video_url=new_task.video_url,
        tests_type=new_task.tests_type,
        simple_test_data=new_task.simple_test_data,
        solution=new_task.solution,
        solution_for_testing=new_task.solution_for_testing
    )
    
    session.add(task)

    await session.commit()
    await session.refresh(task)
    
    print(f'{task.id=}')
    
    return ReadTaskModel.from_orm(task)
