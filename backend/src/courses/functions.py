from typing import Any

from sqlalchemy import select, insert, any_
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import FunctionElement
from fastapi.responses import JSONResponse
from loguru import logger

from ..auth.database import User
from .database import Course, engine


__all__ = (
    "get_course_by_id",
    "create_new_course",
    "get_course_by_id",
    "get_top_of_courses",
    "json_by_course_obj",
    "get_courses_by_role",
)


class json_array_length(FunctionElement):
    name = 'json_array_len'


@compiles(json_array_length)
def compile(element, compiler, **kw):
    return "json_array_length(%s)" % compiler.process(element.clauses)


async def get_course_by_id(course_id: int) -> Course:
    async with engine.connect() as connection:
        db_answer = await connection.execute(select(Course).where(Course.id == course_id))
        return db_answer.fetchone()


async def create_new_course(title: str, description: str, user: User) -> int:
    async with engine.connect() as connection:
        await connection.execute(
            insert(Course)
            .values(
                teachers_ids = [user.id],
                title = title,
                description = description,
            )
        )
        await connection.commit()

        # Fix me: Добавить возвращение присвоенного id


async def get_course_by_param_func(param: str, value: Any) -> Course:
    if param == 'id':
        value = int(value)
    logger.warning(f'{param=}, {value=}')
    async with engine.connect() as connection:
        db_answer = await connection.execute(select(Course).where(param == value))
        return db_answer.fetchone()


async def get_top_of_courses(count: int) -> list[Course]:
    async with engine.connect() as connection:
        db_answer = await connection.execute(
            select(Course)
            .where(Course.is_active is True)
            .order_by(func.json_array_length(Course.passed_id), Course.rating, json_array_length(Course.reviews), json_array_length(Course.passing_id))
            .limit(count)
        )
        return db_answer


async def json_by_course_obj(course_obj: Course) -> dict[Any]:
    return {
        'id': course_obj.id,
        'teachers_ids': course_obj.teachers_ids,
        'titel': course_obj.title,
        'description': course_obj.description,
        'created_at': course_obj.created_at,
        'is_active': course_obj.is_active,
        'course_data': course_obj.course_data,
        'reviews': course_obj.reviews,
        'ico_url': course_obj.ico_url,
        'rating': course_obj.rating,
    }


async def get_courses_by_role(role: str, user: User) -> list[dict[Any]] | JSONResponse:
    if role not in ['student', 'teacher', 'all']:
        return JSONResponse({'message': 'invalid role'}, status_code=400)

    async with engine.connect() as connection:
        if role == 'student':
            request = select(Course).where(Course.passing_id[(user.id,)] is not None)
        elif role == 'teacher':
            request = select(Course).where(Course.teachers_ids[(user.id,)] is not None)
        else:
            request = select(Course).where(Course.teachers_ids[(user.id,)] is not None or Course.passing_id[(user.id,)] is not None)

        db_answer = await connection.execute(request)
        db_answer = db_answer.fetchall()
    
    print([print(type(i)) for i in db_answer])
    res = []
    for i in db_answer:
        res.append(await json_by_course_obj(i))
        if user.id in i.teachers_ids:
            res[-1]['role'] = 'teacher'
        elif user.id in i.reviewspassing_id:
            res[-1]['role'] = 'student'
    return res
