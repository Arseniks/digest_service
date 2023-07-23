"""Конфигурация и настройка бд"""
from __future__ import annotations

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from digest_service.config import settings


class Base(DeclarativeBase):
    pass


class DbConfig:
    """Класс конфигурации подключения к базе данных"""

    _self = None

    def __new__(cls, *args, **kwargs) -> DbConfig:  # noqa:ANN002, ANN003
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self, db_connection_uri: str) -> None:
        self.db_uri = db_connection_uri
        self.engine = None

    def get_engine(self) -> AsyncEngine:
        """Получение движка к текущей базе"""
        if not self.engine:
            self.engine = create_async_engine(settings.DB_CONNECTION_URI, echo=False)
        return self.engine

    def session_factory(self) -> AsyncSession:
        """Получение сессии подключения к базе"""
        engine = self.get_engine()
        return async_sessionmaker(engine)()

    async def get_db(self):
        """Получение бд"""
        async with self.get_engine().begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        db = self.session_factory()
        try:
            yield db
        finally:
            await db.close()


DB_DATA = DbConfig(db_connection_uri=settings.DB_CONNECTION_URI)
