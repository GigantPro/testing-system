import asyncio
import shutil
import urllib.request
from datetime import datetime
from os import makedirs, system
from subprocess import PIPE, STDOUT, run

from loguru import logger
from sqlalchemy import select

from src.config import config
from src.database import Task, async_session_maker

__all__ = ("TaskCheck",)


class NoCodeForRun(Exception):  # noqa: N818
    pass


class TaskCheck:
    def __init__(self, task_id: int) -> None:
        logger.trace(f'Task check created ({task_id})')
        self.task_id = task_id

        self.finished = None
        self.checking = False
        self.task_corutune = None


    async def start(self) -> None:
        logger.info(f'Task check starting ({self.task_id})')
        self.task_corutune = asyncio.run_coroutine_threadsafe(self.check(), asyncio.get_event_loop())


    async def stop(self) -> None:
        logger.info(f'Task check stopped ({self.task_id})')
        self.checking = False
        self.task_corutune.cancel()


    @logger.catch
    async def check(self) -> None:
        async with async_session_maker() as session:
            self.checking = True
            logger.info(f'Task check started ({self.task_id})')
            self.task = (await session.scalars(
                select(Task).where(Task.id == self.task_id))).one()

            self.task.status = 'processing'
            await session.commit()

            makedirs(f'../tmp/{self.task_id}', exist_ok=True)
            system(f'cp docker_tests/Dockerfile.Python ../tmp/{self.task_id}/Dockerfile')

            if self.task.url_code_for_run:
                urllib.request.urlretrieve(self.task.url_code_for_run, f'../tmp/{self.task_id}/solution.py')

            elif self.task.s_code_for_run:
                with open(f'../tmp/{self.task_id}/solution.py', 'w') as f:
                    f.write(self.task.s_code_for_run)

            else:
                logger.error(f'No code for run ({self.task_id})')
                self.task.status = 'error'
                await session.commit()
                self.checking = False
                try:
                    raise NoCodeForRun(f'No code for run ({self.task_id})')
                except NoCodeForRun as ex:
                    # await send_error_msg(ex, self.task.request, 500)
                    logger.error(ex)
                    self.finished = True
                    return

            build_out = run(
                f'docker build -t solution-{self.task_id} ../tmp/{self.task_id}'.split(),
                stdout=PIPE, stderr=STDOUT, text=True)
            run_out = run(
                f'docker run solution-{self.task_id}'.split(),
                stdout=PIPE, stderr=STDOUT, text=True)

            self.task.build_output = build_out.stdout
            self.task.result = run_out.stdout
            self.task.status = 'success'
            self.task.result_getted_time = datetime.now()

            if self.task.correct_output == self.task.result:
                self.task.correct = True

            else:
                self.task.correct = False

                corr_tmp = list(self.task.correct_output)
                output_tmp = list(self.task.result)

                combo = False
                res = 'Incorrect output: >error<:\n'
                for i in range(min((len(corr_tmp), len(output_tmp)))):
                    if corr_tmp[i] == output_tmp[i]:
                        if combo:
                            res += '<'
                            combo = False
                        res += corr_tmp[i]
                    else:
                        if not combo:
                            res += '>'
                            combo = True
                        res += output_tmp[i]
                self.task.incorrect_log = res

            await session.commit()

        shutil.rmtree(f'../tmp/{self.task_id}', ignore_errors=(not config.debug))
        logger.success(f'Task check finished ({self.task_id})')
        self.finished = True
        self.checking = False
