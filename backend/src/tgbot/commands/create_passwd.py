import random
import string

from loguru import logger
from telebot.types import Message

from src.config import config

from ..bot import bot
from ..global_tg_vars import passwords

__all__ = (
    "send_create_passwd",
)


@bot.message_handler(commands=['create_passwd'])
async def send_create_passwd(message: Message) -> None:
    logger.trace('Triggered command /create_passwd')
    if message.from_user.id == config.tg_bot_admin_id:
        new_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        passwords.append(new_code)
        await bot.send_message(message.chat.id, "New temp password: " + new_code)
        logger.info(f'{message.from_user.id} created new temp password: {new_code}')

    else:
        logger.info(f'{message.from_user.id} try to create new temp password')
        await bot.send_message(message.chat.id, "You are not admin")
