import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def hello() -> str:
        return "hello world"


__all__ = ["Query"]
