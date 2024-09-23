FROM python:3.11.10-alpine
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry
COPY . /app
RUN poetry install --no-interaction --no-root
CMD ["pytest", "-s", "-v"]
