FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create directories
RUN mkdir -p input output

# Pre-download the model to avoid runtime downloads
RUN python scripts/download_model.py

# Disable network
RUN pip config set global.trusted-host ""
ENV PYTHONPATH=/app
ENV TRANSFORMERS_OFFLINE=1
ENTRYPOINT ["python", "-u", "src/cli.py"]
CMD ["--help"]