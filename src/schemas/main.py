import strawberry
from strawberry.fastapi import GraphQLRouter
from .queries import Query


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
