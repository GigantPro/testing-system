from fastapi import APIRouter


__all__ = (
    "courses_router",
)

courses_router = APIRouter(prefix='/course')
