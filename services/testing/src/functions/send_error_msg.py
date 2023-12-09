# ruff: noqa: W605

import sys

import aiohttp
from loguru import logger

__all__ = ("send_error_msg",)


@logger.catch
async def send_error_msg(exc: Exception, task_id: int) -> None:
    exc_type, exc_obj, _ = sys.exc_info()

    trace = []
    tb = exc.__traceback__
    while tb is not None:
        trace.append({
            "filename": tb.tb_frame.f_code.co_filename,
            "name": tb.tb_frame.f_code.co_name,
            "lineno": tb.tb_lineno
        })
        tb = tb.tb_next

    tr_exc = [i for i in trace if '/app/src' in i['filename']][-1]

    data = {
        'notify_message': '*Error from tests* \n*Exception:* \{exc\}\n'\
            '*Exception type:* \{exception_type\}\n' \
            '*Exception object:* \{exception_object\}\n' \
            '*Exception file path:* \{exception_fpath\}\n' \
            '*Exception function:* \{exception_func\}\n' \
            '*Exception args:* \{exception_args\}\n' \
            '*Task ID*: \{task_id\}',
        'params': {
            '\{exc\}': str(exc),
            '\{exception_type\}': str(exc_type),
            '\{exception_object\}': str(exc_obj),
            '\{exception_fpath\}': str(tr_exc['filename']) + ':' + str(tr_exc['lineno']),
            '\{exception_func\}': str(tr_exc['name']),
            '\{exception_args\}': str(exc.args),
            '\{task_id\}': str(task_id),
        }
    }

    async with aiohttp.ClientSession() as session:
        async with session.post('http://notify:5001/send_custom_notify', json=data) as resp:
            answer = await resp.text()
    logger.info(answer)
