FROM python:3.12-slim-bullseye

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry \
    && poetry install --no-interaction --no-root \
    &&  poetry run playwright install \
    && playwright install-deps

COPY . /app

CMD ["poetry", "run", "pytest", "-s", "-v", "--alluredir", "allure-results"]
