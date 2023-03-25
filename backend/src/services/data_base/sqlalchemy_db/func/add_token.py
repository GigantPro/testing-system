from ..base import session
from ..tables import SessionToken


__all__ = ("add_token",)

def add_token(token: str, user_id: int = -1) -> None:
    tk = SessionToken(
        None,
        token,
        user_id if user_id != -1 else None,
    )
    session.add(tk)
    session.commit()
    return None
