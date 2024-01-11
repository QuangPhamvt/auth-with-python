import strawberry
from .queries import Query

schema = strawberry.Schema(Query)
__all__ = ["schema"]
