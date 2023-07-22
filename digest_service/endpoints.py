from uuid import UUID

from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from digest_service.db.db_config import DB_DATA
from digest_service.db.schema import Post, Subscription


app = FastAPI()


@app.get("/get_digest/{user_id}/")
async def get_digest(user_id: UUID, db: AsyncSession = Depends(DB_DATA.get_db)):
    """Получение дейджайста по id пользователя"""
    user_subscription_ids = await db.execute(
        select(Post).join(Subscription).where(Post.popularity >= 50, Subscription.user_id == user_id)
    )
    return user_subscription_ids.scalars().all()
