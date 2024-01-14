import strawberry
from strawberry.extensions.tracing import ApolloTracingExtensionSync
from .queries import Query
from .mutations import Mutation


schema = strawberry.Schema(Query, Mutation, extensions=[ApolloTracingExtensionSync])
__all__ = ["schema"]
