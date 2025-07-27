from sentence_transformers import SentenceTransformer, util
import torch

def embed_texts(texts, model_name: str):
    """Embed texts using the specified model."""
    if not texts:  # Handle empty input
        return torch.empty((0, 384))  # Return empty tensor with correct dimensions
    model = SentenceTransformer(model_name)
    return model.encode(texts, convert_to_tensor=True)

def compute_similarity(query_emb, section_embs):
    """Compute cosine similarity between query and section embeddings."""
    if section_embs.shape[0] == 0:  # Handle empty section embeddings
        return []
    return util.cos_sim(query_emb, section_embs).tolist()[0]
