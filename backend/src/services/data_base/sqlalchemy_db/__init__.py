from typing import NoReturn

from .func import select_all, add_token, check_correct_accaunt
from .tables import User, SessionToken
from .base import Base, engine, session


def init_database() -> None | NoReturn:
    Base.metadata.create_all(engine)
    session.commit()
