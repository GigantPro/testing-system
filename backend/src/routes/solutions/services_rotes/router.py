from fastapi import APIRouter

from src.config import config

__all__ = (
    "services_router",
)

services_router = APIRouter(
    prefix='/services', tags=['services'], include_in_schema=config.debug
)
