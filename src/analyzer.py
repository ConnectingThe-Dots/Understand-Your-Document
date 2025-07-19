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