"""Микросервис для создания дейджайстов"""
import argparse

import uvicorn

from digest_service.config import settings
from digest_service.endpoints import app


def main() -> None:
    description = "Микросервис для создания дейджайстов\n\n" "RESTapi документация по пути \\docs\\ "
    formatter = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(
        prog="digest_service",
        description=description,
        formatter_class=formatter,
    )
    parser.add_argument(
        "--db_connection_uri",
        default=settings.DB_CONNECTION_URI,
        type=str,
        help=f"полный URI для бд PostgreSQL [по умолчанию: {settings.DB_CONNECTION_URI}]",
    )
    parser.add_argument(
        "--port",
        default=settings.BACKEND_PORT,
        type=int,
        help=f"привязать сокет к этому порту [по умолчанию: {settings.BACKEND_PORT}]",
    )
    args = parser.parse_args()
    settings.DB_CONNECTION_URI = args.db_connection_uri
    settings.BACKEND_URL_WITH_PORT = f"{settings.BACKEND_URL}:{args.port}"

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=args.port,
        log_level="info",
    )


if __name__ == "__main__":
    main()
