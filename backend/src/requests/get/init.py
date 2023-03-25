from ...app import app
from ...services import check_token, User

from fastapi import Response, Request


__all__ = ('login',)

@app.post('/login')
async def login(login: str, passhash: str, response: Response, request: Request) -> dict:
    if not check_token(response, request):
        return {"error": "Some sort of error with the session key. Get it again."}
    
    