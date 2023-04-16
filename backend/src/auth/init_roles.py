from .database import async_session_maker, Role


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

async def init_roles(session = async_session_maker) -> None:
    __session = session.begin().async_session
    for role_ in __standart_roles:
        __session.add(Role(**role_))

    await __session.commit()
