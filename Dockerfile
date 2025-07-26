FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY config/ ./config
COPY src/* ./

# Create directories
RUN mkdir input output

# Disable network
RUN pip config set global.trusted-host ""
ENV PYTHONPATH=/app
ENTRYPOINT ["python", "-u", "cli.py"]
CMD ["--help"]