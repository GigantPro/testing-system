import asyncio
import shutil
import urllib.request
from datetime import datetime
from os import makedirs, system
from subprocess import PIPE, STDOUT, CompletedProcess, TimeoutExpired, run

from loguru import logger
from sqlalchemy import select

from src.config import config
from src.database import Task, async_session_maker
from src.functions import send_error_msg

__all__ = ("TaskCheck",)


class NoCodeForRun(Exception):  # noqa: N818
    pass


class TaskCheck:
    def __init__(self, task_id: int, checking_ids: list) -> None:
        logger.trace(f'Task check created ({task_id})')
        self.task_id = task_id

        self.finished = False
        self.task_corutune = None
        self.checking_ids = checking_ids

    async def start(self) -> None:
        self.task_corutune = asyncio.run_coroutine_threadsafe(self._start(), asyncio.get_event_loop())

    @logger.catch
    async def _start(self) -> None:
        logger.info(f'Task check starting ({self.task_id})')
        try:
            await self.check()
            logger.info(f'Task check complited ({self.task_id})')

        except Exception as ex:
            logger.exception(ex)
            async with async_session_maker() as session:
                self.task = (await session.scalars(
                    select(Task).where(Task.id == self.task_id))).one()
                self.task.status = 'error'
                await session.commit()

            await send_error_msg(ex, self.task_id)
            logger.error(f'Task check failed ({self.task_id})!')

        finally:
            self.finished = True
            self.checking_ids.remove(self.task_id)


    async def cancel(self) -> None:
        logger.info(f'Task check canceld ({self.task_id})')
        self.task_corutune.cancel()
        self.checking_ids.remove(self.task_id)


    async def check(self) -> None:
        async with async_session_maker() as session:
            logger.info(f'Task check started ({self.task_id})')
            self.task = (await session.scalars(
                select(Task).where(Task.id == self.task_id))).one()

            self.task.status = 'processing'
            await session.commit()

            makedirs(f'../tmp/{self.task_id}', exist_ok=True)
            system(f'cp docker_tests/Dockerfile.Python ../tmp/{self.task_id}/Dockerfile')

            if self.task.url_code_for_run:
                system(f'cp /solutions/{self.task.url_code_for_run.split("/")[-1]} ../tmp/{self.task_id}/solution.py')

            else:
                logger.error(f'No code for run ({self.task_id})')
                self.task.status = 'error'
                await session.commit()
                try:
                    raise NoCodeForRun(f'No code for run ({self.task_id})')
                except NoCodeForRun as ex:
                    await send_error_msg(ex, self.task_id)
                    logger.error(ex)
                    self.finished = True
                    return

            build_out = run(
                f'docker build -t solution-{self.task_id} ../tmp/{self.task_id}'.split(),
                stdout=PIPE, stderr=STDOUT, text=True)
            try:
                run_out: CompletedProcess[str] = run(
                    f'docker run '\
                        f'-m {self.task.extra_params["memory_limit"]}MB '\
                        f'--cpus={self.task.extra_params["cpu_limit"]} '\
                        f'solution-{self.task_id}'.split(),
                    stdout=PIPE, stderr=STDOUT, text=True, timeout=self.task.extra_params['time_limit'])

            except TimeoutExpired:
                self.task.status = 'success'
                self.task.correct = False
                self.task.incorrect_log = 'Timeout'
                self.task.build_output = build_out.stdout
                self.task.result_getted_time = datetime.now()
                await session.commit()
                return


            self.task.build_output = build_out.stdout
            self.task.result = run_out.stdout
            self.task.result_getted_time = datetime.now()

            if run_out.returncode != 0:
                self.task.status = 'error'
                self.task.correct = False

                self.task.incorrect_log = run_out.stderr
                await session.commit()
                return

            self.task.status = 'success'

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
