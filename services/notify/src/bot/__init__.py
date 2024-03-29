# ruff: noqa: F403, F401

import asyncio

from .bot import bot
from .commands import *
from .send_notify import send_notify


async def start_bot() -> asyncio.Future:
    n_thread = asyncio.run_coroutine_threadsafe(bot.polling(), asyncio.get_event_loop())
    return n_thread
