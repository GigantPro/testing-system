from ..base import session
from ..tables import User


__all__ = ("check_correct_accaunt",)

def check_correct_accaunt(login: str, passhash: str) -> bool:
    accaunt = session.query(User).filter(User.login == login).first()
    if not accaunt:
        return False
    elif accaunt.passhash != passhash:
        return False
    return True
