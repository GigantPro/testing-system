from .delete import init_delete
from .post import init_post
from .get import init_get


__all__ = ("init_requests",)


def init_requests() -> None:
    """
    Initialize the requests module.
    """
    init_post()
    init_get()
    init_delete()