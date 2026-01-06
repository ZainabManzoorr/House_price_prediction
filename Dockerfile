FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN RUN poetry install --only main
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
