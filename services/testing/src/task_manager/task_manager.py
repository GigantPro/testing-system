import asyncio

from loguru import logger
from sqlalchemy import select

from src.config import config
from src.database import Task, get_async_session

from .task_check import TaskCheck

__all__ = ("TaskManager",)


class TaskManager:
    def __init__(self) -> None:
        self.working = False

        self.max_tasks = config.parallel_tests_max
        self.tasks = []

    async def start(self) -> None:
        logger.info('Task manager started')
        self.working = True
        async for session in get_async_session():
            tasks: list[tuple[Task]] = (await session.execute(
                select(Task)
                .where(Task.status == 'processing')
                .order_by(Task.priority.desc())
            )).fetchall()

            while self.working:
                new_ls = []
                for i in range(len(self.tasks)):
                    if not self.tasks[i].finished and self.tasks[i].checking:
                        new_ls += [self.tasks[i]]
                self.tasks = new_ls.copy()
                del new_ls

                while len(self.tasks) < self.max_tasks and tasks:
                    task = tasks.pop()
                    task_check = TaskCheck(task[0].id)
                    self.tasks.append(task_check)
                    await task_check.start()

                if not tasks:
                    tasks = (await session.execute(
                        select(Task)
                        .where(Task.status == 'created')
                        .order_by(Task.priority.desc())
                    )).fetchall()

                await asyncio.sleep(1)

    async def stop(self) -> None:
        self.working = False
        for task in self.tasks:
            await task.stop()
        self.tasks = []
