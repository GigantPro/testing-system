from loguru import logger

from src.config import config

from .bot import bot
from .global_tg_vars import users_ides


async def send_notify(message: str) -> tuple[int, int]:
    """Send notify for loggined users

    Args:
        message (str): message to send

    Returns:
        tuple[int, int]: num of sent messages, num of not sent messages
    """
    logger.info(f'Send notify: {message}')

    good, bad = 0, 0

    for user_id in users_ides:
        try:
            await bot.send_message(user_id, message, parse_mode="MarkdownV2")
            logger.info(f'Sended error notify to {users_ides[user_id]}|{user_id}')
            good += 1
        except Exception as ex:
            logger.error(f'Error notify to {users_ides[user_id]}|{user_id} : {ex}')
            bad += 1

    await bot.send_message(
        config.tg_bot_admin_id,
        f'Message sent to *{good}* users\. Failed send to *{bad}* users\.',
        parse_mode="MarkdownV2"
    )

    return good, bad
