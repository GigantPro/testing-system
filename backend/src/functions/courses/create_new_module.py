from fastapi.responses import JSONResponse
from sqlalchemy import insert, select, update

from src.database import Course, CourseData, Module, User, engine
from src.types import CourseFullModel, CreateModuleModel, FullCourseDataModel, ReadModuleModel

__all__ = ("create_new_module",)

async def create_new_module(course_id: int, new_module: CreateModuleModel, user: User) -> JSONResponse | ReadModuleModel:  # noqa: E501
    async with engine.connect() as connection:
        course = await connection.execute(
            select(Course)
            .where(Course.id == course_id)
        )
        course = course.fetchone()

        if not course:
            return JSONResponse(status_code=404, content={"message": "Course not found"})

        course = CourseFullModel.from_orm(course)

        if user.id not in course.teachers_ids:
            return JSONResponse(status_code=403, content={"message": "User is not a teacher of the course"})

        course_data = await connection.execute(
            select(CourseData)
            .where(CourseData.id == course.course_data_id)
        )

        course.course_data = FullCourseDataModel.from_orm(course_data.fetchone())

        _new_module = await connection.execute(
            insert(Module)
            .values(
                title=new_module.title,
                description=new_module.description,
            )
            .returning(Module)
        )
        _new_module = _new_module.fetchone()
        _new_module = ReadModuleModel.from_orm(_new_module)

        await connection.execute(
            update(CourseData)
            .where(CourseData.id == course.course_data.id)
            .values(modules = [*course.course_data.modules_ids, _new_module.id])
        )

        await connection.commit()
    return _new_module
