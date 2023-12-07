from src.config import config


__all__ = (
    "secret_validate",
)

async def secret_validate(secret: str) -> bool:
    return secret == config.tests_api_secret