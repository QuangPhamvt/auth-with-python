from sqlalchemy import select
from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession
import strawberry
from src.database import User
from src.dependencies.helpers import hash_password


@strawberry.input
class InputSignup:
    username: str
    password: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def signup(self, input: InputSignup, info: Info) -> str:
        username, password = input.username, input.password
        statement = select(User).filter_by(username=username)
        db: AsyncSession = info.context["db"]
        user_obj = (await db.execute(statement)).scalars().all()
        if len(user_obj):
            return "Username is exist"
        hashpw = hash_password(password=password)
        user = User(username=username, hash_password=hashpw)
        db.add(user)
        await db.commit()
        return f"{username} - {hashpw}"
