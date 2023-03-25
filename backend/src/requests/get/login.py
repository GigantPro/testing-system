from ...app import app
from ...services import check_correct_accaunt

from fastapi import Response, Request


__all__ = ('login',)

@app.post('/login')
async def login(login: str, passhash: str, response: Response, request: Request) -> dict:
    if check_correct_accaunt(login, passhash):
        return {"result": "sucscess"}
    else:
        return {"result": "error"}