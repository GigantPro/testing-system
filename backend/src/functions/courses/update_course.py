from fastapi.responses import JSONResponse
from sqlalchemy import select, update

from src.database import Course, User, engine
from src.types import CourseUpdateModel

__all__ = ("update_course",)

async def update_course(updated_course: CourseUpdateModel, user: User) -> JSONResponse:
    async with engine.connect() as connection:
        original_course = await connection.execute(
            select(Course)
            .where(Course.id == updated_course.id)
        )
        original_course: Course = original_course.fetchone()

        if user.id not in original_course.teachers_ids:
            return JSONResponse({'message': 'You are not a teacher', 'status': 'error'}, 403)

        change_dict = {}
        for var, value in updated_course.dict().items():
            if value and var not in ('id',):
                change_dict[var] = value


        await connection.execute(
            update(Course)
            .where(Course.id == original_course.id)
            .values(**change_dict)
        )

        await connection.commit()

        return JSONResponse({'status': 'success'}, 200)
