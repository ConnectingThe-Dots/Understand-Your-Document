FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY config/ ./config
RUN mkdir input output

ENV PYTHONPATH=/app
ENTRYPOINT ["python", "-u", "-m", "src.cli"]
CMD ["--help"]
