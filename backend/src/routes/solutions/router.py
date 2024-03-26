from fastapi import APIRouter

from .services_rotes import services_router

__all__ = (
    "solution_router",
)

solution_router = APIRouter(prefix='/solutions')

solution_router.include_router(services_router)
