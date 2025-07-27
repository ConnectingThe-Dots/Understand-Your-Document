from sentence_transformers import SentenceTransformer, util

def embed_texts(texts, model_name):
    model = SentenceTransformer(model_name)
    return model.encode(texts, convert_to_tensor=True)

def compute_similarity(query_emb, section_embs):
    return util.cos_sim(query_emb, section_embs).tolist()[0]
