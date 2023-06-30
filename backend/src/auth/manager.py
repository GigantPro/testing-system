from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas

from .database import User, get_user_db
from .funcstions import _get_user_by_username
from ..db_config import config

SECRET = config.SECRET_MANAGER


class CustomUserAlreadyExist(exceptions.FastAPIUsersException):
    pass


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f'User {user.id} has registered.')

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f'User {user.id} has forgot their password. Reset token: {token}')

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f'Verification requested for user {user.id}. Verification token: {token}')

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:        
        await self.validate_password(user_create.password, user_create)
        
        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )

        existing_user = await self.user_db.get_by_email(user_create.email)
        existing_user = await _get_user_by_username(user_dict['username']) if not existing_user else existing_user
        if existing_user:
            raise exceptions.UserAlreadyExists()

        
        password = user_dict.pop('password')
        user_dict['hashed_password'] = self.password_helper.hash(password)
        user_dict['role_id'] = 1
        user_dict['ico_url'] = user_dict['ico_url'] if user_dict.get('ico_url', None) else '/api/static/standart_ico.png'

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
