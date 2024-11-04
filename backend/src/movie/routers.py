

from fastapi import APIRouter, Depends, HTTPException
from src.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from src.movie.models import movie

router = APIRouter(prefix="/movies", tags=["movie"])

@router.get("")
async def get_movies(count: int = 12, session: AsyncSession = Depends(get_async_session)):
    try:
        query = sa.select(movie).limit(count)
        result = await session.execute(query)
        return {
            "status": "ok",
            "data": result.all(),
            "message": None
        }

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "message": None
        })
