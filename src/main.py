from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from src.schemas import schema
from src.dependencies import get_context


graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
