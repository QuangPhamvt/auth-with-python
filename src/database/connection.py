from sqlalchemy import URL, create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

url_create = URL.create(
    drivername="mysql+asyncmy",
    username="root",
    password="123456",
    host="127.0.0.1",
    port=3306,
    database="PYTHON",
)

engine = create_async_engine(url_create, echo=True)
engine_base = create_engine(
    "mysql+pymysql://root:123456@127.0.0.1:3306/PYTHON", echo=True
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine_base)

SessionLocal = async_sessionmaker(autoflush=False, bind=engine)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
