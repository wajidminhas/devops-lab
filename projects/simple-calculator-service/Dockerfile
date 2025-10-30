# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project file
COPY pyproject.toml .

COPY . .  

# Install dependencies
RUN uv sync

# Copy application

# Expose port
EXPOSE 8003

# Run
CMD [".venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]