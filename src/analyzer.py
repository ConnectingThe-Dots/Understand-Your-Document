import yaml
from sklearn.cluster import KMeans
import numpy as np
import re
from typing import List, Dict

from src.utils import setup_logger
import logging

logger = logging.getLogger(__name__)


def load_config(path: str = "config/default.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def filter_noise(items: List[Dict], patterns: List[str]) -> List[Dict]:
    regexes = [re.compile(p) for p in patterns]
    return [itm for itm in items if not any(r.match(itm["text"]) for r in regexes)]


def cluster_font_sizes(items: List[Dict], config: dict) -> List[int]:
    sizes = np.array([itm["size"] for itm in items]).reshape(-1, 1)
    n_clusters = min(config["clustering"]["n_clusters"], len(items))
    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=config["clustering"]["random_state"],
    )
    labels = kmeans.fit_predict(sizes)
    centers = kmeans.cluster_centers_.flatten()
    # sort clusters by center size desc
    order = np.argsort(-centers)
    rank = {order[i]: i+1 for i in range(len(order))}
    return [rank[label] for label in labels]


def assign_levels(items: List[Dict], config: dict) -> List[Dict]:
    items = filter_noise(items, config.get("ignore_patterns", []))
    levels = cluster_font_sizes(items, config)
    top_n = config["heading_rules"]["top_n_clusters"]
    result = []
    for itm, lvl in zip(items, levels):
        if lvl <= top_n:
            words = itm["text"].split()
            if len(words) <= 8 and (itm["text"].istitle() or itm["text"].isupper()):
                itm["level"] = lvl
                result.append(itm)
    return result

import yaml, re
import numpy as np
from sklearn.cluster import KMeans
from typing import List, Dict
from src.embedding import embed_texts, compute_similarity

def load_config(path="config/default.yaml") -> dict:
    return yaml.safe_load(open(path))

def filter_noise(items, patterns):
    regs = [re.compile(p) for p in patterns]
    return [i for i in items if not any(r.match(i["text"]) for r in regs)]

def cluster_font_sizes(items, cfg):
    if not items:
        return []
    sizes = np.array([i["size"] for i in items]).reshape(-1,1)
    km = KMeans(n_clusters=min(cfg["clustering"]["n_clusters"], len(items)),
                random_state=cfg["clustering"]["random_state"])
    labels = km.fit_predict(sizes)
    centers = km.cluster_centers_.flatten()
    order = np.argsort(-centers)
    rank = {order[i]: i+1 for i in range(len(order))}
    return [rank[l] for l in labels]

def assign_levels(items, cfg) -> List[Dict]:
    items = filter_noise(items, cfg["ignore_patterns"])
    if not items:
        return []
    levels = cluster_font_sizes(items, cfg)
    result=[]
    for itm, lvl in zip(items, levels):
        if lvl<=cfg["heading_rules"]["top_n_clusters"]:
            words=itm["text"].split()
            if len(words)<=8 and (itm["text"].istitle() or itm["text"].isupper()):
                itm["level"]=lvl
                result.append(itm)
    return result

def chunk_sections(headings: List[Dict], max_chars: int) -> List[Dict]:
    secs=[]; cur=None
    for h in headings:
        if h["level"]==1:
            if cur: secs.append(cur)
            cur={"title":h["text"],"page":h["page"],"text":h["text"],"level":1}
        else:
            if cur and cur["level"]<h["level"]:
                cur["text"] += " " + h["text"]
        if cur and len(cur["text"])>max_chars:
            cur["text"] = cur["text"][:max_chars-3] + "..."
    if cur: secs.append(cur)
    return secs

def score_sections(sections: List[Dict], persona: Dict) -> List[Dict]:
    texts=[s["text"] for s in sections]
    sec_emb = embed_texts(texts, persona["embed_model"])
    query = persona.get("description","")+" "+persona.get("job_to_be_done","")
    q_emb = embed_texts([query], persona["embed_model"])[0]
    scores = compute_similarity(q_emb, sec_emb)
    out=[]
    for sec, sc in zip(sections, scores):
        if sc>=persona["relevance_threshold"]:
            sec["importance_rank"]=round(float(sc),3)
            out.append(sec)
    return sorted(out, key=lambda x:-x["importance_rank"])
