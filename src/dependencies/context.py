from fastapi import Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from src.database.connection import get_db


async def get_context(db: AsyncSession = Depends(get_db)):
    return {"db": db}
