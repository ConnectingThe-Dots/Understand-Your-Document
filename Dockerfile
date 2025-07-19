FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src/ ./src
COPY config/ ./config

# Create directories
RUN mkdir input output

# Disable network
RUN pip config set global.trusted-host ""

ENTRYPOINT ["python", "-u", "src/cli.py"]
CMD ["--help"]