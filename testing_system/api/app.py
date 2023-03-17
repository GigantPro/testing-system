from fastapi import FastAPI
from .config import config


__all__ = ("app",)

app = FastAPI()
