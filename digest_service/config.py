"""Модель класса для параметров по умолчанию."""
import os

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    DB_CONNECTION_URI: str = os.environ.get(
        "DB_CONNECTION_URI",
        "postgresql+asyncpg://postgres:postgres@localhost:5432/dev_db",
    )
    BACKEND_URL: str = os.environ.get("BACKEND_URL", "http://localhost")
    BACKEND_PORT: str = os.environ.get("BACKEND_PORT", "5001")
    BACKEND_URL_WITH_PORT: str = f"{BACKEND_URL}:{BACKEND_PORT}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = AppSettings()
