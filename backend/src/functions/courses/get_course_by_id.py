from fastapi.responses import JSONResponse
from sqlalchemy import select

from src.database import Course, engine
from src.types import CourseFullModel

__all__ = ("get_course_by_id",)

async def get_course_by_id(course_id: int) -> CourseFullModel:
    async with engine.connect() as connection:
        db_answer = await connection.execute(select(Course).where(Course.id == course_id))
    answer = db_answer.fetchone()

    if answer:
        return CourseFullModel.from_orm(answer)
    return JSONResponse(status_code=404, content={"message": "Course not found"})
