# Document Understanding System - Challenge 1A

This project processes PDF documents and extracts their structure using advanced NLP techniques.

## Prerequisites

- Python 3.9+
- pip (Python package manager)
- Docker (optional, for containerized running)

## Project Structure

```
Understand-Your-Document/
│
├── input/                         # Place your PDF files here
├── output/                        # Generated JSON files will be stored here
├── config/                        # Configuration files
├── models/                        # Pre-downloaded models (sentence-transformers)
├── src/                           # Source code
├── scripts/                       # Utility scripts (bench.py, download_model.py)
├── tests/                         # Test files (unit and integration tests)
├── connecting_the_dots.egg-info/  # Package installation info
├── Dockerfile                     # Docker configuration
├── pyproject.toml                 # Project configuration
├── setup.py                       # Package setup file
└── requirements.txt               # Python dependencies
```

## Installation & Running
### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/ConnectingThe-Dots/Understand-Your-Document.git
```

### Option 1: Running with Docker

1. Navigate to the Understand-Your-Document directory:
```bash
cd Understand-Your-Document
```

2. Build the Docker image:
```bash
docker build -t connecting-dots .
```

3. Run the container:
```bash
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output connecting-dots --config config/default.yaml
```

### Option 2: Running Locally

1. Navigate to the Understand-Your-Document directory:
```bash
cd Understand-Your-Document
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```

4. Run the application:
```bash
python -m src.cli --config config/default.yaml
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
# Navigate to Understand-Your-Document directory first
cd Understand-Your-Document

# Local execution
python -m src.cli --config config/default.yaml --input-dir input --output-dir output

# Docker execution
docker run -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output connecting-dots --config config/default.yaml --input-dir input --output-dir output
```

## Technical Documentation

### Architecture Overview

The Document Understanding System follows a modular architecture designed for processing PDF documents and extracting structured information using advanced NLP techniques.

### Core Components

#### 1. Document Parser (`src/parser.py`)
- Extracts text and metadata from PDF documents
- Handles various PDF formats and structures
- Preserves document layout and hierarchical information

#### 2. Text Embedding System (`src/embedding.py`)
- Uses sentence-transformers for semantic text representation
- Computes similarity scores between text sections
- Enables semantic search and content matching

#### 3. Document Analyzer (`src/analyzer.py`)
- Processes extracted text using NLP techniques
- Identifies document structure and key sections
- Applies persona-based analysis for targeted extraction

#### 4. Output Serializer (`src/serializer.py`)
- Converts processed data to structured JSON format
- Maintains document hierarchy and relationships
- Ensures consistent output schema

### Machine Learning Model

#### Sentence Transformer Model
- **Model**: `all-MiniLM-L6-v2`
- **Purpose**: Text embedding and semantic similarity computation
- **Architecture**: Multi-layer transformer optimized for sentence-level representations
- **Dimensions**: 384-dimensional embeddings
- **Performance**: Balanced accuracy and efficiency for document understanding tasks

#### Model Features
- Pre-trained on diverse text corpora
- Optimized for semantic textual similarity
- Lightweight and fast inference
- Suitable for real-time document processing

### Libraries and Dependencies

#### Core NLP Libraries
- **sentence-transformers** (≥2.2.2): Semantic text embeddings and similarity computation
- **transformers**: Hugging Face transformer models and utilities
- **torch**: PyTorch deep learning framework for model inference

#### Document Processing
- **PyPDF2** / **pdfplumber**: PDF text extraction and parsing
- **python-docx**: Microsoft Word document processing
- **beautifulsoup4**: HTML/XML parsing and text extraction

#### Data Processing
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing and array operations
- **scikit-learn**: Machine learning utilities and preprocessing

#### Configuration and CLI
- **click**: Command-line interface framework
- **PyYAML**: YAML configuration file parsing
- **python-dotenv**: Environment variable management

#### Development and Testing
- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Code linting and style checking

### Processing Pipeline

1. **Document Ingestion**: PDF files are loaded and validated
2. **Text Extraction**: Content is extracted while preserving structure
3. **Preprocessing**: Text is cleaned and segmented into meaningful sections
4. **Embedding Generation**: Text sections are converted to semantic embeddings
5. **Analysis**: Content is analyzed based on specified persona and job requirements
6. **Similarity Matching**: Relevant sections are identified using cosine similarity
7. **Output Generation**: Results are structured and serialized to JSON format

### Configuration

The system uses YAML configuration files to define:
- Model parameters and settings
- Processing pipeline options
- Input/output directory specifications
- Logging levels and formats
- Persona descriptions and job definitions

### Performance Considerations

- **Model Caching**: Pre-downloaded models for offline operation
- **Batch Processing**: Efficient handling of multiple documents
- **Memory Management**: Optimized for large document processing
- **Containerization**: Docker support for consistent deployment

---

**Built for Adobe India Hackathon - Challenge 1A**
***
## Team vector
