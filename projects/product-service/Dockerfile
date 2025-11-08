FROM python:3.10-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
COPY pyproject.toml .
COPY . .

# Install dependencies (including httpx)
RUN uv sync

# Expose port
EXPOSE 8002

# Run with global uvicorn (not .venv/bin/uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]