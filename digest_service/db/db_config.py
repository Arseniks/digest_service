from __future__ import annotations

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, AsyncSession, create_async_engine

from digest_service.config import settings


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

    def session_factory(self):
        """Получение сессии подключения к базе"""
        engine = self.get_engine()
        return async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


DB_DATA = DbConfig(db_connection_uri=settings.DB_CONNECTION_URI)
