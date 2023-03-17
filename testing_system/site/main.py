from typing import NoReturn

from .config import config
from .app import app
from .requests import init_requests


def main() -> NoReturn:
    init_requests()
    
    app.run(
        host=config.ip,
        port=config.port,
        debug=config.debug,
    )
