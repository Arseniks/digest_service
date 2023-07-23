FROM python:3.10

RUN mkdir /digest_service

WORKDIR /digest_service

RUN pip install poetry
COPY poetry.lock pyproject.toml /digest_service/
RUN poetry config virtualenvs.create false && poetry install

COPY . .

RUN chmod a+x /digest_service/docker/*.sh

