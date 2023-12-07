from loguru import logger
from telebot.async_telebot import AsyncTeleBot

from ..config import config

API_TOKEN = config.tg_bot_token

bot = AsyncTeleBot(API_TOKEN)
logger.info('Tg bot initialized')
