from typing import NoReturn

from .config import config
from .requests import init_requests

import uvicorn


def main() -> NoReturn:
    init_requests()
    
    uvicorn.run(
        "src.app:app",
        host=config.ip,
        port=config.port,
        log_level=config.log_level,
    )
