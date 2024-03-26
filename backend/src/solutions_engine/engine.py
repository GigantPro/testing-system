import asyncio
import aiohttp
from loguru import logger
from sqlalchemy import select

from src.config import config
from src.types import ServiceTaskModel
from src.database import get_async_session, Solution, Task


__all__ = (
    "solutions_engine",
    "SolutionsEngine",
)

class SolutionsEngine:
    def __init__(self) -> None:
        self.engine = None
        self.checking = False
        self.checking_solutions = {}
        """{solut_id: {corutine, tasks_ids: [int], tasks: list[ServiceTaskModel]}}"""


    async def start(self) -> None:
        self.checking = True
        self.engine = asyncio.run_coroutine_threadsafe(self._start(), asyncio.get_event_loop())

    
    async def stop(self) -> None:
        logger.info('Solutions engine stopped')
        self.checking = False
        self.engine.cancel()
        for sol_id in self.checking_solutions:
            self.checking_solutions[sol_id]['corutine'].cancel()
        self.checking_solutions.clear()


    async def check_solution(self, solution: Solution) -> None:
        logger.info(f'Start checking solution: {solution.id=} {solution.user_id=} {solution.task_id=}')
        cor = asyncio.run_coroutine_threadsafe(self._check_solution(solution), asyncio.get_event_loop())
        self.checking_solutions[solution.id] = {'corutine': cor}
        

    async def _check_solution(self, solution: Solution) -> None:
        async for session in get_async_session():
            session.begin()
            
            solution = (await session.scalar(select(Solution).where(Solution.id == solution.id))).one()
            task = (await session.scalar(select(Task).where(Task.id == solution.task_id))).one()

            if solution.status == 'checking':
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'http://tests:5001/task_by_id?task_id={solution.testing_task_id}&secret=1') as resp:
                        answer = await resp.text()

            logger.info(answer)

    
    @logger.catch
    async def _start(self) -> None:
        logger.info('Solutions engine started')

        tasks = []
        async for session in get_async_session():
            session.begin()
            tasks = (await session.scalars(select(Solution).where(Solution.status == 'checking'))).all()
            logger.warning(f'Found {len(tasks)} tasks ({tasks=})')
            
        while self.checking:
            while len(self.checking_solutions) < config.max_parallel_solition_jobs and tasks:
                new_task = tasks.pop(0)
                if new_task.id not in self.checking_solutions:
                    await self.check_solution(new_task)

            await asyncio.sleep(1)
            if not tasks:
                async for session in get_async_session():
                    session.begin()
                    tasks = (await session.scalars(select(Solution).where(Solution.status == 'created'))).all()
                    logger.warning(f'Found {len(tasks)} tasks ({tasks=})')


solutions_engine = SolutionsEngine()
