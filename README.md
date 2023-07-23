# digest_service

## Описание проекта
Микросервис, который будет формировать дайджесты контента для
пользователей на основе их подписок. Дайджест представляет 
собой выборку постов из различных источников, на которые подписан пользователь.

## Что внутри?
### Документация API
Документация, описанная в формате openapi лежит в поднятом сервисе по обработчику `/docs`
### Структура проекта
```
digest_service - код приложения
├── db
│   ├── db_config.py - конфигурация бд
│   └── schema.py    - бд модели алхимии
├── __main__.py - запуск всего сервиса
├── config.py - класс конфигурации проекта
└── endpoints.py - endpoint-ы приложения
docker - скрипты для докера
migration - миграции для базы данных
```

## Копирование проекта
- Клонируйте проект с GitHub с помощью команды:
```commandline
git clone https://github.com/Arseniks/digest_service
```
- Перейдите в папку с проектом:
```commandline
cd digest_service
```

## Запуск проекта с помощью Docker-a
- Создаем контейнер
```
docker compose build
```
- Запускаем контейнер
```
docker compose up 
```

## Запуск проекта вручную
### На Windows
- Скопируйте файл .env.template в .env, при необходимости отредактируйте 
  значения переменных:
```
copy .env.template .env
``` 
- Добавление виртуальной среды venv:
```
python -m venv venv
``` 
- Активация виртуальной среды
```
venv\Scripts\activate.bat
``` 
- Установите poetry
```
pip install poetry
```
- Установка зависимостей:
```
poetry install
```
- Установка миграций alembic:
```
alembic upgrade head
```
### На Linux/Mac
- Скопируйте файл .env.template в .env, при необходимости отредактируйте значения переменных:
```
cp .env.template .env
```
- Добавление виртуальной среды venv:
```
python3 -m venv venv
```
- Активация виртуальной среды
```
source venv/bin/activate
```
- Установите poetry
```
pip3 install poetry
```
- Установка зависимостей:
```
poetry install
```
- Установка миграций alembic:
```
alembic upgrade head
```
### Запуск сервиса
    usage: digest_service [-h] [--db_connection_uri DB_CONNECTION_URI] [--port PORT]
      
    options:
      -h, --help                            показать это сообщение
      --db_connection_uri DB_CONNECTION_URI полный URI для бд PostgreSQL 
                                            [по умолчанию: postgresql+asyncpg://postgres:postgres@localhost:5432/dev_db]
      --port PORT                           привязать сокет к этому порту [по умолчанию: 5001]
