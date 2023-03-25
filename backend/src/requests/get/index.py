from ...app import app

from fastapi.responses import RedirectResponse


__all__ = ('index',)

@app.get('/')
async def index():
    return RedirectResponse("/docs")
