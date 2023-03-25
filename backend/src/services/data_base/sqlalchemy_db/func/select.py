from typing import NoReturn, Any

from ..base import session


__all__ = ("select_all",)

def select_all(table: Any) -> list | NoReturn:
    query = session.query(table)
    return query.all()
    