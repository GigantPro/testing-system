FROM python:3.10.10-alpine3.17 as python-base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.4.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

FROM python-base as poetry-base

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

FROM python-base as backend

COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

# Add Poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

RUN apk update && \
    apk upgrade

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-interaction --no-cache --without dev

COPY ./src ./
COPY ./public ./public

CMD ["poetry", "run", "uvicorn",  "--reload",  "--host", "0.0.0.0",  "--port", "5001", "src.app:app"]

