import json

from loguru import logger
from telebot.types import Message

from ..bot import bot
from ..global_tg_vars import passwords, users_ides

__all__ = (
    "send_login",
)


@bot.message_handler(commands=['login'])
async def send_login(message: Message) -> None:
    logger.trace('Triggered command /login')

    passwd = message.text.replace('/login', '').strip()

    logger.trace(f'/login: Inputed password: {passwd}')

    if passwd in passwords and message.from_user.id not in users_ides:
        with open('users_ides.json', 'w') as f:
            users_ides[message.from_user.id] = message.from_user.username
            json.dump(users_ides, f)
        passwords.remove(passwd)
        await bot.send_message(message.chat.id, "Login success")
        logger.info(f'{message.from_user.id} logged in')

    elif message.from_user.id in users_ides:
        try:
            passwords.remove(passwd)
            logger.trace(f'/login: Removed password: {passwd}')
        except:  # noqa: E722
            pass

        await bot.send_message(message.chat.id, "You are already logged in!\nPassword was removed")
        logger.info(f'{message.from_user.id} try to login again')

    else:
        await bot.send_message(message.chat.id, "Wrong password")
        logger.info(f'{message.from_user.id} try to login with wrong password')
