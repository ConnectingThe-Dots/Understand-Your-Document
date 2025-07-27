# Challenge 1B - Document Analysis with Persona-Driven Processing

A sophisticated document analysis system that processes PDF collections and extracts relevant sections based on specific personas and job requirements.

## 🚀 Features

- **PDF Processing**: Extract text and structure from PDF documents
- **Persona-Driven Analysis**: Score document sections based on relevance to specific roles and tasks
- **Batch Processing**: Handle multiple collections of documents simultaneously
- **Flexible Output**: Generate structured JSON output with rankings and metadata
- **Docker Support**: Containerized deployment for consistent environments
- **CLI Interface**: Easy-to-use command-line interface

## 📋 Prerequisites

- Python 3.12+
- Docker (optional, for containerized deployment)
- Git

## 🛠️ Installation

### Option 1: Local Python Environment

1. **Clone the repository:**
```bash
git clone https://github.com/ConnectingThe-Dots/Understand-Your-Document.git
cd Understand-Your-Document/challenge_1B
```

2. **Create and activate virtual environment:**
```bash
cd /path/to/Connecting_the_Dots
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install the package:**
```bash
cd challenge_1B
pip install -e .
```

### Option 2: Docker Environment

1. **Build the Docker image:**
```bash
cd challenge_1B
docker build -t challenge_1b_image .
```

## 📁 Project Structure

```
challenge_1B/
├── config/
│   └── default.yaml          # Configuration file
├── src/
│   ├── cli.py                # Command-line interface
│   ├── multi_processor.py    # Batch collection processor
│   ├── analyzer.py           # Document analysis logic
│   ├── parser.py             # PDF parsing utilities
│   ├── embedding.py          # Text embedding functions
│   ├── serializer.py         # Output formatting
│   └── utils.py              # Utility functions
├── scripts/
│   ├── run_collections.sh    # Native collection processing script
│   └── docker_run_collections.sh  # Docker collection processing script
├── input/                    # Input PDF files (for individual processing)
├── output/                   # Output JSON files
├── Challenge_1b/             # Collections directory
│   ├── Collection 1/
│   ├── Collection 2/
│   └── Collection 3/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── setup.py
└── README.md
```

## 🎯 Usage

### Individual PDF Processing

#### Native Python
```bash
# Activate virtual environment
source .venv/bin/activate
cd challenge_1B

# Basic processing
python -m src.cli

# With persona and job description
python -m src.cli \
  --persona-desc "Data Analyst" \
  --job "Extract financial metrics and trends"

# Custom directories and config
python -m src.cli \
  --config config/default.yaml \
  --input-dir input \
  --output-dir output \
  --persona-desc "Research Scientist" \
  --job "Identify key research findings" \
  --log-level DEBUG
```

#### Docker
```bash
# Show help
docker run --rm challenge_1b_image

# Process with persona
docker run --rm \
  -v "$(pwd)/input:/app/challenge_1B/input" \
  -v "$(pwd)/output:/app/challenge_1B/output" \
  -v "$(pwd)/config:/app/challenge_1B/config" \
  challenge_1b_image \
  --config config/default.yaml \
  --input-dir input \
  --output-dir output \
  --persona-desc "Travel Planner" \
  --job "Plan a 4-day trip for college friends"
```

### Collections Processing

#### Native Python
```bash
# Using the script
source .venv/bin/activate
cd challenge_1B
./scripts/run_collections.sh

# Direct command
source .venv/bin/activate
cd /path/to/Connecting_the_Dots
python -m challenge_1B.src.multi_processor \
  --config challenge_1B/config/default.yaml \
  --collections-root challenge_1B/Challenge_1b
```

#### Docker
```bash
# Using the Docker script
cd challenge_1B
./scripts/docker_run_collections.sh

# Direct Docker command
docker run --rm \
  --entrypoint="" \
  -v "$(pwd)/Challenge_1b:/app/challenge_1B/Challenge_1b" \
  -v "$(pwd)/config:/app/challenge_1B/config" \
  challenge_1b_image \
  python -m challenge_1B.src.multi_processor \
  --config challenge_1B/config/default.yaml \
  --collections-root challenge_1B/Challenge_1b
```

#### Docker Compose
```bash
docker-compose up --build
```

## 📄 Input Format

### Individual Processing
Place PDF files in the `input/` directory. The system will process all PDF files found.

### Collections Processing
Each collection should follow this structure:
```
Challenge_1b/
├── Collection 1/
│   ├── challenge1b_input.json
│   ├── PDFs/
│   │   ├── document1.pdf
│   │   ├── document2.pdf
│   │   └── ...
│   └── challenge1b_output.json (generated)
├── Collection 2/
│   └── ...
```

**challenge1b_input.json format:**
```json
{
  "persona": {
    "role": "Travel Planner"
  },
  "job_to_be_done": {
    "task": "Plan a trip of 4 days for a group of 10 college friends."
  },
  "documents": [
    {"filename": "document1.pdf"},
    {"filename": "document2.pdf"}
  ]
}
```

## 📊 Output Format

### Individual Processing
```json
{
  "title": "document.pdf",
  "metadata": {
    "pages": 15,
    "generated_at": "2025-07-27T10:30:00+05:30",
    "config_used": "config/default.yaml"
  },
  "extracted_sections": [
    {
      "title": "Section Title",
      "page": 5,
      "importance_rank": 0.85
    }
  ],
  "outline": [
    {
      "level": "1",
      "text": "Chapter 1: Introduction",
      "page": 1
    }
  ]
}
```

### Collections Processing
```json
{
  "metadata": {
    "input_documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "Travel Planner",
    "job_to_be_done": "Plan a trip..."
  },
  "extracted_sections": [
    {
      "document": "doc1.pdf",
      "section_title": "Best Destinations",
      "importance_rank": 1,
      "page_number": 3
    }
  ],
  "subsection_analysis": [
    {
      "document": "doc1.pdf",
      "refined_text": "Chapter 1: Overview",
      "page_number": 1
    }
  ]
}
```

## ⚙️ Configuration

Edit `config/default.yaml` to customize:

```yaml
# Clustering settings
clustering:
  n_clusters: 5
  random_state: 42

# Persona settings
persona:
  embed_model: "sentence-transformers/all-MiniLM-L6-v2"
  relevance_threshold: 0.3
  max_section_chars: 2000
  description: ""
  job_to_be_done: ""
```

## 🐳 Docker Commands Reference

### Build Commands
```bash
# Build image
docker build -t challenge_1b_image .

# Build with docker-compose
docker-compose build
```

### Run Commands
```bash
# CLI help
docker run --rm challenge_1b_image

# Individual processing
docker run --rm \
  -v "$(pwd)/input:/app/challenge_1B/input" \
  -v "$(pwd)/output:/app/challenge_1B/output" \
  challenge_1b_image \
  --persona-desc "Analyst" --job "Extract data"

# Collections processing
docker run --rm --entrypoint="" \
  -v "$(pwd)/Challenge_1b:/app/challenge_1B/Challenge_1b" \
  challenge_1b_image \
  python -m challenge_1B.src.multi_processor \
  --config challenge_1B/config/default.yaml \
  --collections-root challenge_1B/Challenge_1b
```

## 🔧 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Ensure virtual environment is activated
   source .venv/bin/activate
   
   # Reinstall package
   cd challenge_1B && pip install -e .
   ```

2. **Docker Permission Issues**
   ```bash
   # Ensure Docker is running
   sudo systemctl start docker
   
   # Add user to docker group
   sudo usermod -aG docker $USER
   ```

3. **Memory Issues with Large PDFs**
   ```bash
   # Increase Docker memory limit or process files individually
   docker run --memory=4g --rm challenge_1b_image
   ```

### Logs and Debugging

```bash
# Enable debug logging
python -m src.cli --log-level DEBUG

# Check Docker logs
docker logs <container_id>

# Verbose output
docker run --rm -it challenge_1b_image /bin/bash
```

## 📝 CLI Options

### Individual Processing (`src.cli`)
- `--config`: Path to configuration file (default: `config/default.yaml`)
- `--input-dir`: Input directory containing PDFs (default: `input`)
- `--output-dir`: Output directory for JSON files (default: `output`)
- `--persona-desc`: Description of the persona/role
- `--job`: Job or task to be accomplished
- `--log-level`: Logging level (DEBUG, INFO, WARNING, ERROR)

### Collections Processing (`src.multi_processor`)
- `--config`: Path to configuration file (default: `config/default.yaml`)
- `--collections-root`: Root directory containing Collection folders (default: `.`)

## 🧪 Testing

```bash
# Run with sample data
cd challenge_1B
echo "Test PDF processing..." > input/test.txt
python -m src.cli --persona-desc "Tester" --job "Test the system"

# Verify output
ls -la output/
cat output/test.json
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is part of the Adobe India Hackathon Challenge.

## 📞 Support

For issues and questions:
- Create an issue in the GitHub repository
- Check the troubleshooting section above
- Review configuration settings

---

**Built for Adobe India Hackathon - Challenge 1B**
