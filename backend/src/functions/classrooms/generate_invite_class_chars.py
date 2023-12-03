import random
from string import ascii_lowercase, ascii_uppercase

from sqlalchemy import select

from src.database import ClassInvite, engine

__all__ = ("generate_invite_class_chars",)

async def generate_invite_class_chars() -> str:
    """Fenerate unique charset with len=10

    Returns:
        str: unique generated charset
    """
    async with engine.connect() as connection:
        while True:
            generated_code = ''.join(
                [random.choice(ascii_lowercase + ascii_uppercase + '0123456789') for _ in range(10)]
            )
            data = await connection.execute(select(ClassInvite).where(ClassInvite.invite_code == generated_code))
            data = data.fetchone()
            if not data:
                return generated_code
