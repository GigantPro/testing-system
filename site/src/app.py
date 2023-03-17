from flask import Flask
from .config import config


__all__ = ("app",)

app = Flask(__name__, template_folder=config.source_path)
