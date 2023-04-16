from sqlalchemy import select, insert

from .database import engine, Role


__standart_roles = [
    {
        "id": 1,
        "name": "student",
        "permissions": None
    },
    {
        "id": 2,
        "name": "admin",
        "permissions": None
    },
    {
        "id": 3,
        "name": "creator",
        "permissions": None
    }
]

async def init_roles() -> None:
    async with engine.connect() as connection:
        for role_ in __standart_roles:
            if not await connection.execute(select(Role).where(Role.id == role_['id'])):
                await connection.execute(insert(Role).values(**role_))
        await connection.commit()
