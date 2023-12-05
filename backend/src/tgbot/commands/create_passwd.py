import random
import string
from telebot.types import Message

from ..bot import bot
from src.config import config
from ..global_tg_vars import passwords

__all__ = (
    "send_create_passwd",
)


@bot.message_handler(commands=['create_passwd'])
async def send_create_passwd(message: Message):
    if message.from_user.id == config.tg_bot_admin_id:
        new_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        passwords.append(new_code)
        await bot.send_message(message.chat.id, "New temp password: " + new_code)

    else:
        await bot.send_message(message.chat.id, "You are not admin")
