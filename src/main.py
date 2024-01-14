from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio.session import AsyncSession
from strawberry.fastapi import GraphQLRouter

from src.database.connection import get_db

from .schemas import schema


async def get_context(db: AsyncSession = Depends(get_db)):
    return {"db": db}


graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
