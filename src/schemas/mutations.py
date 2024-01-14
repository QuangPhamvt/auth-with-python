import bcrypt
from typing import Annotated, Union
from src.database import User as User_tbl
from src.dependencies.helpers import hash_password
from sqlalchemy import select
import strawberry
from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession


@strawberry.type
class User:
    def __init__(self, id: str, username: str) -> None:
        self.id = id
        self.username = username

    id: str
    username: str


@strawberry.type
class RegisterUserSuccess:
    def __init__(
        self,
        user: User,
    ) -> None:
        self.user = user

    user: User


@strawberry.type
class UsernameAlreadyExistsError:
    def __init__(self, alternative_username: str) -> None:
        self.alternative_username = alternative_username

    alternative_username: str


Response = Annotated[
    Union[RegisterUserSuccess, UsernameAlreadyExistsError],
    strawberry.union("RegisterUserResponse"),
]


@strawberry.type
class LoginUserSuccess:
    def __init__(self, user: User) -> None:
        self.user = user

    user: User


@strawberry.type
class PasswordError:
    def __init__(self, message: str) -> None:
        self.message = message

    message: str


@strawberry.type
class UsernameError:
    def __init__(self, message: str) -> None:
        self.message = message

    message: str


LoginResponse = Annotated[
    Union[LoginUserSuccess, PasswordError, UsernameError],
    strawberry.union("LoginUSerResponse"),
]


@strawberry.input
class InputRegisterUser:
    username: str
    password: str


@strawberry.input
class InputLoginUser:
    username: str
    password: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def registerUser(self, input: InputRegisterUser, info: Info) -> Response:
        db: AsyncSession = info.context["db"]
        username, password = input.username, input.password
        statement = select(User_tbl).filter_by(username=username)
        user_obj = (await db.execute(statement)).scalars().all()
        if len(user_obj):
            return UsernameAlreadyExistsError("Exists Username")
        hashpw = hash_password(password)
        print(hashpw)
        user = User_tbl(username, hashpw)
        db.add(user)
        await db.commit()
        return RegisterUserSuccess(User("123", username))

    @strawberry.mutation
    async def loginUser(self, input: InputLoginUser, info: Info) -> LoginResponse:
        db: AsyncSession = info.context["db"]
        username, password = input.username, input.password
        statemane = select(User_tbl).filter_by(username=username)
        user_obj = (await db.execute(statemane)).scalar()
        if type(user_obj) is not User_tbl:
            return UsernameError("Username doesn't exist")

        _byte = bytes(str(user_obj.hash_password), "utf-8")
        print(_byte)
        is_checkpw = bcrypt.checkpw(password.encode("utf-8"), _byte)
        if is_checkpw:
            return LoginUserSuccess(User(str(user_obj.id), user_obj.username))
        return PasswordError("PasswordError")


__all__ = ["Mutation"]
