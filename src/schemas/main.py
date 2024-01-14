import strawberry
from strawberry.fastapi import GraphQLRouter

from .queries import Query
from .mutations import Mutation


schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQLRouter(schema)
