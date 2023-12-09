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

            checking_ids = []
            while self.working:
                new_ls = []
                for i in range(len(self.tasks)):
                    if not self.tasks[i].finished and self.tasks[i].checking:
                        new_ls += [self.tasks[i]]
                self.tasks = new_ls.copy()
                del new_ls

                while len(checking_ids) < config.parallel_tests_max and tasks:
                    task = tasks.pop(0)
                    if task[0].id not in checking_ids:
                        checking_ids += [task[0].id]
                        task_check = TaskCheck(task[0].id, checking_ids)
                        await task_check.start()

                await asyncio.sleep(1)

                if not tasks:
                    tasks = (await session.execute(
                        select(Task)
                        .where(Task.status == 'created')
                        .order_by(Task.priority.desc())
                    )).fetchall()

    async def stop(self) -> None:
        self.working = False
        for task in self.tasks:
            await task.stop()
        self.tasks = []
