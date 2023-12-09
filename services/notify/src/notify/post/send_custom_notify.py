from fastapi import Body, Request
from loguru import logger

from src.bot import send_notify
from src.functions import text_preparation

from ..router import notify_router

__all__ = (
    "send_custom_notify",
)

@notify_router.post("/send_custom_notify")
async def send_custom_notify(
    request: Request, notify_message: str = Body(...),
    params: dict[str, str] = Body(...)
)-> dict:
    logger.info(f'Send base notify by {request.client.host}')
    for key, value in params.items():
        notify_message = notify_message.replace(
            key, await text_preparation(value)
        )

    message = str(notify_message)

    good, bad = await send_notify(message)

    return {
        'success': good,
        'failed': bad,
        'message': message
    }
