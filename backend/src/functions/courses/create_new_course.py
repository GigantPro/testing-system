from sqlalchemy import insert, update

from src.database import get_async_session, User, Course, CourseData
from src.types import CourseUserReadModel, CourseFullModel


__all__ = ("create_new_course",)

async def create_new_course(title: str, description: str, user: User) -> CourseUserReadModel:
    async for session in get_async_session():
        course = Course(
            teachers_ids = [user.id],
            title = title,
            description = description,
        )
        
        session.add(course)
        await session.commit()

        course_data_id = await session.execute(
            insert(CourseData)
            .values(
                course_id = course.id,
            )
            .returning(CourseData.id)
        )

        await session.execute(
            update(Course)
            .where(Course.id == course.id)
            .values(
                course_data_id = course_data_id.scalar_one(),
            )
        )

        await session.commit()

        return CourseUserReadModel.from_orm(course)
