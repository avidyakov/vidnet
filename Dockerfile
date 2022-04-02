FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false
EXPOSE 8000/tcp
WORKDIR /app

RUN pip3 install poetry

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-ansi
