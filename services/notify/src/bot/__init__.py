# ruff: noqa: F403

import asyncio

from .bot import bot
from .commands import *


async def start_bot() -> asyncio.Future:
    n_thread = asyncio.run_coroutine_threadsafe(bot.polling(), asyncio.get_event_loop())
    return n_thread
