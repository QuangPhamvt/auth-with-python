from sqlalchemy.orm import DeclarativeBase
from connect import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    pass


class Profile(Base):
    pass


Base.metadata.create_all(bind=engine)
