import strawberry
from strawberry.extensions.tracing import ApolloTracingExtensionSync
from .queries import Query
from .mutations import Mutation


schema = strawberry.Schema(
    query=Query, mutation=Mutation, extensions=[ApolloTracingExtensionSync]
)
__all__ = ["schema"]
