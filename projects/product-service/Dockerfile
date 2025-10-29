

# Dockerfile
FROM python:3.10-slim

WORKDIR /app


RUN pip install uv
# Copy pyproject.toml (and poetry.lock if you have it)
COPY pyproject.toml .

# Install dependencies using uv (fast!) or pip
RUN  uv pip install  --no-cache-dir .

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]