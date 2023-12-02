from fastapi.responses import JSONResponse
from sqlalchemy import update, select

from src.database import engine, Course, User
from src.types import CreateModuleModel, CourseFullModel


__all__ = ("create_new_module",)

async def create_new_module(course_id: int, new_module: CreateModuleModel, user: User) -> JSONResponse:
    async with engine.connect() as connection:
        course = await connection.execute(
            select(Course)
            .where(Course.id == course_id)
        )
        course = course.fetchone()
        print(f'{course=}')
        print(f'{course.course_data=}')
        c_s = course
        
        if not course:
            return JSONResponse(status_code=404, content={"message": "Course not found"})

        course = CourseFullModel.from_orm(course)
        
        if user.id not in course.teachers_ids:
            return JSONResponse(status_code=403, content={"message": "User is not a teacher of the course"})
        
        print(f'{course=}')
        print(f'{c_s=}')
        
        await connection.commit()
