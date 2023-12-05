from sys import stdout

from loguru import logger

from .config import config


async def init_logger() -> None:
    if config.debug:  # Если переменная True - значит дебажим. Здесь не нужен not
        logger.add(
            stdout,
            format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}",
            level='trace',
            backtrace=True,
            colorize=True,
            enqueue=True,
        )

    else:
        logger.add(
            "logs/log.json",
            format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}",
            level=10,
            serialize=True,
            rotation="500 MB",
            compression="zip",
            backtrace=True,
            enqueue=True,
        )
    
    logger.info("Logger initialized")
