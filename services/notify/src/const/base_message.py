from pydantic import BaseModel

__all__ = (
    "BaseMessageModel",
    "base_message_template",
)

base_message_template = """*{title_error_msg}* in *{t_service_name}*
*URL:* {requested_url}
*Method:* {requested_method}
*Exception type:* {exception_type}
*Exception object:* {exception_object}
*Exception fpath:* {exception_fpath}
*Exception func:* {exception_func}
*Exception args:* {exception_args}
*IP:* {ip}
*PORT:* {port}
*User\-Agent:* {user_agent}
"""

class BaseMessageModel(BaseModel):
    title_error_msg: str
    t_service_name: str
    requested_url: str
    requested_method: str
    exception_type: str
    exception_object: str
    exception_fpath: str
    exception_func: str
    exception_args: str
    ip: str
    port: str
    user_agent: str
