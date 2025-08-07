from engine.store import VectorStore
import numpy as np


def test_basic_add_and_search():
    store = VectorStore(max_size=3)
    store.add("doc1", [0.1, 0.2, 0.3])
    store.add("doc2", [0.2, 0.3, 0.4])
    store.add("doc3", [0.9, 0.9, 0.9])

    results = store.search([0.1, 0.2, 0.3], k=2)
    assert len(results) == 2
    assert results[0][0] in {"doc1", "doc2"}
