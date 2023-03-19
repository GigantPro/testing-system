from hashlib import sha256
from random import random
from datetime import datetime

from .data_base import add_token

from fastapi import Response, Request


__all__ = ("check_teken")

def check_token(response: Response, request: Request) -> bool:
    session_key = request.cookies.get('sessionKey')
    if not session_key:
        new_key = sha256(
            f'{random()}'
            f'{datetime.now().ctime()}'
            f'{response.body.decode("ascii")}'.encode('ascii')
        ).hexdigest()
        add_token(new_key)
        return True
    
    return True
