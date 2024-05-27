import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from .db import User, get_user_db

SECRET = "SECRET"


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        """
        在用户注册后调用的异步函数。
        参数:
            self：类实例。
            user（user）：注册的用户对象。
            request（可选[request]，可选）：与注册关联的请求对象。默认为“无”。
        """
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        """
        在用户忘记密码后触发以处理重置过程。
        参数:
            user（user）：忘记密码的用户。
            token（str）：为密码重置生成的重置令牌。
            request（可选[request]，可选）：与密码重置相关联的请求。默认为“无”。
        """
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        """
            在用户发送请求前 对用户进行验证
        """
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    """
    产生UserManager实例的异步生成器。
    ：param user_db：用户数据库依赖项。
    ：type user_db:Any
    ：return：UserManager实例。
    ：rtype:UserManager
    """
    yield UserManager(user_db)
