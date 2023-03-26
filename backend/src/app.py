from fastapi import FastAPI
from .config import config


app = FastAPI(
    title="Study Organized",
    debug=config.debug,
)
