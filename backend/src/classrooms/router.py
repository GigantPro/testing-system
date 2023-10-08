from fastapi import APIRouter


__all__ = (
    "classrooms_router",
)

classrooms_router = APIRouter(prefix='/classroom')
