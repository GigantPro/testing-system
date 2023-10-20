from sqlalchemy import select
from fastapi.responses import JSONResponse

from src.database import engine, Course, User
from src.types import CourseFullModel


__all__ = ("get_courses_by_role",)

async def get_courses_by_role(role: str, user: User) -> list[CourseFullModel] | JSONResponse:
    if role not in ['student', 'teacher', 'all']:
        return JSONResponse({'message': 'invalid role'}, status_code=400)

    async with engine.connect() as connection:
        if role == 'student':
            request = select(Course).where(Course.passing_id[(user.id,)] is not None)
        elif role == 'teacher':
            request = select(Course).where(Course.teachers_ids[(user.id,)] is not None)
        else:
            request = select(Course).where(Course.teachers_ids[(user.id,)] is not None or \
                Course.passing_id[(user.id,)] is not None)

        db_answer = await connection.execute(request)
        db_answer = db_answer.fetchall()

    res = []
    for i in db_answer:
        res.append(CourseFullModel.from_orm(i))
        if user.id in i.teachers_ids:
            res[-1].role = 'teacher'
        elif user.id in i.reviewspassing_id:
            res[-1].role = 'student'
    return res
