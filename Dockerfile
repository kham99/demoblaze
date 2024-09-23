FROM python:3.12-slim-bullseye

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install --no-cache-dir poetry
COPY . /app
RUN poetry install --no-interaction --no-root



CMD ["poetry", "run", "pytest", "-s", "-v"]
