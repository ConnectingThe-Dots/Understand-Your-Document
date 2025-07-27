FROM python:3.12-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire challenge_1B directory structure
COPY . ./challenge_1B/
COPY config/ ./challenge_1B/config/
COPY src/ ./challenge_1B/src/
COPY scripts/ ./challenge_1B/scripts/

# Create necessary directories
RUN mkdir -p challenge_1B/input challenge_1B/output

# Install the package in development mode
RUN cd challenge_1B && pip install -e .

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Default entrypoint for CLI
ENTRYPOINT ["python", "-m", "challenge_1B.src.cli"]
CMD ["--help"]
