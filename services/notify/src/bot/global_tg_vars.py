import json

from loguru import logger

passwords = []

try:
    with open('users_ides.json', 'r') as f:
        users_ides = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    users_ides = {}
    with open('users_ides.json', 'w') as fs:
        fs.write(json.dumps(users_ides))

logger.info('Global Tg vars initialized')
