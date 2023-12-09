from fastapi import Request
from loguru import logger

from src.bot import send_notify
from src.const import BaseMessageModel, base_message_template
from src.functions import text_preparation

from ..router import notify_router

__all__ = (
    "send_base_notify",
)

@notify_router.post("/send_base_notify")
async def send_base_notify(base_message: BaseMessageModel, request: Request) -> dict:
    logger.info(f'Send base notify by {request.client.host}')
    message_args = base_message.model_dump()
    r_message_args = {}
    for key, value in message_args.items():
        r_message_args[key] = await text_preparation(value)

    message = str(base_message_template.format(**r_message_args))

    good, bad = await send_notify(message)

    return {
        'success': good,
        'failed': bad,
        'message': message
    }
