FROM python:3.10-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy project files
COPY pyproject.toml .

RUN pip install fastapi uvicorn httpx

COPY . .

# Install dependencies (including httpx)
# RUN uv sync && \
#     echo '/root/.local/bin' >> /etc/environment

ENV PATH="/root/.local/bin:${PATH}"

# Expose port
EXPOSE 8002

# Run with global uvicorn (not .venv/bin/uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]