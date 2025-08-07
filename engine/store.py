import time
from typing import List, Tuple, Dict, Any, Optional
import heapq
import numpy as np

from .eviction import LRUEvictionPolicy
from .index import cosine_similarity


class VectorStore:
    def __init__(self, max_size: int = 10000, ttl_seconds: Optional[int] = None):
        self.store = {}
        self.metadata = {}
        self.ttl = ttl_seconds
        self.max_size = max_size
        self.eviction_policy = LRUEvictionPolicy()

    def _expire_old_keys(self):
        now = time.time()
        expired_keys = [
            k for k, v in self.store.items()
            if self.ttl and now - v["timestamp"] > self.ttl
        ]
        for key in expired_keys:
            self.delete(key)

    def add(self, id: str, vector: List[float], metadata: Dict[str, Any] = None):
        self._expire_old_keys()
        if len(self.store) >= self.max_size:
            evict_key = self.eviction_policy.evict()
            if evict_key:
                self.delete(evict_key)

        vec_np = np.array(vector, dtype=np.float32)
        self.store[id] = {
            "vector": vec_np,
            "timestamp": time.time(),
        }
        self.metadata[id] = metadata or {}
        self.eviction_policy.record_access(id)

    def search(self, query_vector: List[float], k: int = 5) -> List[Tuple[str, float]]:
        self._expire_old_keys()
        query = np.array(query_vector, dtype=np.float32)

        scored = []
        for id, entry in self.store.items():
            score = cosine_similarity(query, entry["vector"])
            scored.append((id, score))
            self.eviction_policy.record_access(id)

        top_k = heapq.nlargest(k, scored, key=lambda x: x[1])
        return top_k

    def delete(self, id: str):
        self.store.pop(id, None)
        self.metadata.pop(id, None)
        self.eviction_policy.remove(id)

    def snapshot(self, path: str):
        import pickle
        with open(path, 'wb') as f:
            pickle.dump({
                "store": self.store,
                "metadata": self.metadata
            }, f)

    def load(self, path: str):
        import pickle
        with open(path, 'rb') as f:
            data = pickle.load(f)
            self.store = data["store"]
            self.metadata = data["metadata"]
