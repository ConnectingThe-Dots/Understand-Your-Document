# Document Understanding System - Challenge 1A

This project processes PDF documents and extracts their structure using advanced NLP techniques.

## Prerequisites

- Python 3.9+
- pip (Python package manager)
- Docker (optional, for containerized running)

## Project Structure

```
challenge_1A/
│
├── input/               # Place your PDF files here
├── output/             # Generated JSON files will be stored here
├── config/             # Configuration files
├── models/             # Pre-downloaded models
├── src/               # Source code
└── requirements.txt   # Python dependencies
```

## Installation & Running

### Option 1: Running Locally

1. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```

3. Run the application:
```bash
python -m src.cli --config config/default.yaml
```

### Option 2: Running with Docker

1. Build the Docker image:
```bash
docker build -t connecting-dots .
```

2. Run the container:
```bash
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output connecting-dots --config config/default.yaml
```

## Usage

1. Place your PDF files in the `input/` directory
2. Run the application using either of the methods above
3. Check the `output/` directory for generated JSON files

## Command Line Options

```bash
Options:
  --config TEXT        Path to configuration file (default: config/default.yaml)
  --input-dir TEXT    Input directory containing PDF files (default: input)
  --output-dir TEXT   Output directory for JSON files (default: output)
  --persona-desc TEXT Persona description
  --job TEXT          Job to be done
  --log-level TEXT    Logging level (default: INFO)
  --help             Show this message and exit
```

## Example

To process PDFs with a specific configuration:

```bash
# Local execution
python -m src.cli --config config/default.yaml --input-dir input --output-dir output

# Docker execution
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output connecting-dots --config config/default.yaml --input-dir input --output-dir output
```
