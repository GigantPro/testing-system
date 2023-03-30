import asyncio
from typing import NoReturn

from .config import config
from .requests import init_requests
from .services import init_database

import uvicorn


def main() -> NoReturn:
    # init
    asyncio.run(init_database())
    init_requests()
    
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(init_requests())
    
    uvicorn.run(
        "src.app:app",
        host=config.ip,
        port=config.port,
        log_level=config.log_level,
    )
