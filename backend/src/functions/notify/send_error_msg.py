import sys
from fastapi import Request
import aiohttp
from loguru import logger


__all__ = ("send_error_msg",)

async def send_error_msg(exc: Exception, request: Request, error_code: int) -> None:
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
        'title_error_msg': str(error_code),
        't_service_name': 'Backend.Edu.Xiver',
        'requested_url': str(request.url),
        'requested_method': request.method,
        'exception_type': str(exc_type),
        'exception_object': str(exc_obj),
        'exception_fpath': str(tr_exc['filename']) + ':' + str(tr_exc['lineno']),
        'exception_func': str(tr_exc['name']),
        'exception_args': str(exc.args),
        'ip': request.client.host,
        'port': str(request.client.port),
        'user_agent': request.headers['User-Agent'],
    }

    async with aiohttp.ClientSession() as session:
        async with session.post('http://notify:5001/send_base_notify', json=data) as resp:
            answer = await resp.text()
    logger.info(answer)
