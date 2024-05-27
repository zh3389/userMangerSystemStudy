from ctypes import Union

from fastapi_users import BaseUserManager, InvalidPasswordException, UUIDIDMixin
from .db import User
import uuid
from fastapi_users import BaseUserManager, UUIDIDMixin


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    # ...
    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail"
            )
