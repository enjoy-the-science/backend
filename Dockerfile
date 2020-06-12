FROM python:3.8 AS base

RUN pip install --no-cache-dir poetry

WORKDIR /usr/src/app
COPY ./pyproject.toml ./poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev


FROM base AS app

COPY ./backend ./backend


FROM base AS base-dev

RUN poetry install


FROM base-dev AS dev

COPY . .
