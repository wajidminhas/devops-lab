FROM python:3.10-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
# COPY pyproject.toml .


COPY . .

# Create virtual environment and install dependencies
RUN uv sync

# RUN ls -la
# RUN ls -la .venv/bin/ || echo ".venv/bin/ not found"

# Copy the rest of your application

# Use the virtual environment's uvicorn
CMD [".venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]