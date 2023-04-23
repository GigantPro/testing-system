from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, RedirectResponse

from ..auth.database import User
from ..auth.auth import fastapi_users
from .config import config
from .const import URL_FOR_REDIRRECT_AFTER_VERIF_PASSED
from .functions import __update_verification_status


current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)

verification_router = APIRouter(prefix='/verification')

verification_orders = {}

@verification_router.get('/')
async def send_verif_mail(
    verification_code: int = -1,
    user: User = Depends(current_active_user),
) -> dict:
    if verification_code != -1:
        if verification_orders.get(user.id, -1) != verification_code:
            return JSONResponse({'message': 'The code is incorrect or you didn`t ask for it'}, 404)

        await __update_verification_status(user.id)
        verification_orders.pop(user.id)

        return RedirectResponse(URL_FOR_REDIRRECT_AFTER_VERIF_PASSED, 303)

    else:
        with smtplib.SMTP_SSL(config.mail_server, 465) as smtp:
            smtp.login(config.email, config.mail_password)

            verification_orders[user.id] = random.randint(10**10, 10**11)

            url = f'https://edu.xiver.ru/api/user/verification/?verification_code={verification_orders[user.id]}'
            if config.debug:
                url = f'http://localhost/api/user/verification/?verification_code={verification_orders[user.id]}'

            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Verify your account'
            msg['From'] = config.email
            msg['To'] = user.email

            with open('./src/verification/static/verefication_msg.html', 'r', encoding='utf-8') as verif_msg:
                html = verif_msg.read().format(url=url)

            part1 = MIMEText('In order to verify your email, you need to click on this link', 'plain')
            part2 = MIMEText(html, 'html')

            msg.attach(part1)
            msg.attach(part2)

            smtp.sendmail(config.email, user.email, msg.as_string())
        return {'message': 'The message has been sent to the mail'}
