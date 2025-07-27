from sentence_transformers import SentenceTransformer
import os

def download_model():
    print("Downloading and caching model...")
    cache_dir = os.path.join(os.path.dirname(__file__), "..", "models")
    os.makedirs(cache_dir, exist_ok=True)
    model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder=cache_dir)
    print(f"Model cached in: {cache_dir}")

if __name__ == "__main__":
    download_model()
