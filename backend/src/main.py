from typing import NoReturn

from .config import config
from .requests import init_requests
from .services import init_database

import uvicorn


def main() -> NoReturn:
    init_database()
    
    init_requests()
    
    uvicorn.run(
        "src.app:app",
        host=config.ip,
        port=config.port,
        log_level=config.log_level,
    )
