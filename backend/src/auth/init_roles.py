from sqlalchemy import select, insert, update

from ..database import engine, Role


__all__ = ("init_roles", "__standart_roles")

__standart_roles = [
    {
        'id': 1,
        'name': 'student',
        'permissions': None
    },
    {
        'id': 2,
        'name': 'teacher',
        'permissions': {
            'create_classrooms': True
        }
    },
    {
        'id': 3,
        'name': 'tester',
        'permissions': {
            'create_classrooms': True
        }
    },
    {
        'id': 4,
        'name': 'moderator',
        'permissions': {
            'create_classrooms': True
        }
    },
    {
        'id': 5,
        'name': 'admin',
        'permissions': {
            'create_classrooms': True
        }
    },
    {
        'id': 6,
        'name': 'creator',
        'permissions': {
            'create_classrooms': True
        }
    }
]

async def init_roles() -> None:
    async with engine.connect() as connection:
        for role_ in __standart_roles:
            result = await connection.execute(select(Role).where(Role.id == role_['id']))
            if not result.fetchone():
                await connection.execute(insert(Role).values(**role_))
            else:
                await connection.execute(update(Role).where(Role.id == role_['id']).values(**role_))

        await connection.commit()
