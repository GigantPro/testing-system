from loguru import logger
from telebot.types import Message

from ..bot import bot

__all__ = (
    "send_welcome",
)


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message: Message) -> None:
    logger.trace('Triggered command /help or /start')
    await bot.reply_to(message, """\
Hi there, I am Education Errors Bot.
For loggin in use /login [password]\
""")
    logger.info(f'{message.from_user.id} send welcome message')
