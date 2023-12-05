import json
from telebot.types import Message

from ..bot import bot
from ..global_tg_vars import passwords, users_ides

__all__ = (
    "send_welcome",
)


@bot.message_handler(commands=['login'])
async def send_login(message: Message):
    passwd = message.text.replace('/login', '').strip()
    if passwd in passwords and message.from_user.id not in users_ides:
        with open('users_ides.json', 'w') as f:
            users_ides[message.from_user.id] = message.from_user.username
            json.dump(users_ides, f)
        passwords.remove(passwd)
        await bot.send_message(message.chat.id, "Login success")

    elif message.from_user.id in users_ides:
        try: passwords.remove(passwd)
        except: pass

        await bot.send_message(message.chat.id, "You are already logged in!\nPassword was removed")

    else:
        await bot.send_message(message.chat.id, "Wrong password")
