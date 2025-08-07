from engine.store import VectorStore
import numpy as np
import time

store = VectorStore(max_size=100000)

# Generate 100K random vectors
vectors = [np.random.rand(128).tolist() for _ in range(100000)]

start = time.time()
for i, vec in enumerate(vectors):
    store.add(f"vec{i}", vec)
print(f"Insertion time: {time.time() - start:.2f}s")

query = np.random.rand(128).tolist()
start = time.time()
res = store.search(query, k=10)
print(f"Search time: {time.time() - start:.4f}s")
