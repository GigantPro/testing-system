import os
import sys

from fastapi import Request

from .bot import bot
from .global_tg_vars import users_ides


async def send_notify(request: Request, exc: Exception) -> None:
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


    message = "*Internal server error* in *backend*\n" + \
        "*URL:* {}\n" + \
        "*Method:* {}\n" + \
        "{}\n" + \
        "*Exception type:* {}\n" + \
        "*Exception object:* {}\n" + \
        "*Exception fpath:* {}\n" + \
        "*Exception func:* {}\n" + \
        "{}\n" \
        "*IP:* {}\n" \
        "*PORT:* {}\n" \
        "*User\\-Agent:* {}\n" \
        "*Args:* {}"

    params = [
        request.url,
        request.method,
        '---------------------------------',
        str(exc_type),
        str(exc_obj),
        str(tr_exc['filename']) + ':' + str(tr_exc['lineno']),
        str(tr_exc['name']),
        '---------------------------------',
        request.client.host,
        request.client.port,
        request.headers['User-Agent'],
        exc.args
    ]

    for i in range(len(params)):
        params[i] = str(params[i]).replace("_", '\\_') \
            .replace("*", '\\*') \
            .replace("[", '\\[') \
            .replace("]", '\\]') \
            .replace("(", '\\(') \
            .replace(")", '\\)') \
            .replace("~", '\\~') \
            .replace("`", '\\`') \
            .replace(">", '\\>') \
            .replace("#", '\\#') \
            .replace("+", '\\+') \
            .replace("-", '\\-') \
            .replace("=", '\\=') \
            .replace("|", '\\|') \
            .replace("{", '\\{') \
            .replace("}", '\\}') \
            .replace(".", '\\.') \
            .replace("!", '\\!')
    message = message.format(*params)

    for user_id in users_ides:
        await bot.send_message(user_id, message, parse_mode="MarkdownV2")
