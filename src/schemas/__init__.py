import strawberry
from .queries import Query
from .mutations import Mutation

schema = strawberry.Schema(Query, Mutation)
__all__ = ["schema"]
