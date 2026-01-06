# 1️⃣ Base image
FROM python:3.12-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy files
COPY pyproject.toml poetry.lock ./
COPY app ./app

# 4️⃣ Install Poetry
RUN pip install --no-cache-dir poetry

# 5️⃣ Install only prod dependencies
RUN poetry config virtualenvs.create false \
 && poetry install --only main --no-interaction --no-ansi

# 6️⃣ Expose port
EXPOSE $PORT

# 7️⃣ Run Gunicorn to serve Flask
CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:$PORT", "app.app:app"]