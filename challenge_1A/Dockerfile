FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy pre-downloaded model
COPY models/models--sentence-transformers--all-MiniLM-L6-v2 /root/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2

# Copy project files
COPY . .

# Create directories
RUN mkdir -p input output

# Disable network
RUN pip config set global.trusted-host ""
ENV PYTHONPATH=/app
ENV TRANSFORMERS_OFFLINE=1
ENTRYPOINT ["python", "-u", "src/cli.py"]
CMD ["--help"]