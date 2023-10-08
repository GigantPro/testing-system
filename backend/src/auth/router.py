from fastapi import APIRouter

from .verification import verification_router


__all__ = (
    "self_router",
    "upload_router",
    "user_get_router",
)

self_router     = APIRouter(prefix='/self')
upload_router   = APIRouter(prefix='/upload')
user_get_router = APIRouter(prefix='/user')
