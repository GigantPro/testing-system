from pathlib import Path

from fastapi.responses import FileResponse, JSONResponse

from src.config import config
from src.database import User

__all__ = ("get_solution_func",)

async def get_solution_func(
    solution_name: str,
    user: User,
) -> FileResponse:
    if not solution_name.startswith(str(user.id)):
        return JSONResponse(status_code=404, content={'message': 'Permission denided'})

    sol_path = Path(f'{config.solutions_files_path}/{solution_name}')

    if not sol_path.exists():
        return JSONResponse(status_code=404, content={'message': 'Solution not found'})

    return FileResponse(f'{config.solutions_files_path}/{solution_name}')
