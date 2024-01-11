from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .schemas import schema


graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
print("http://127.0.0.1:4000/graphql")
