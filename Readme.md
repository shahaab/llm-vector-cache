# LLM Vector Cache

A blazing-fast in-memory vector store for similarity search with LRU + TTL support. Built in Python for AI caching, search engines, and embedding workloads.

### Features
- Cosine similarity search
- LRU eviction
- TTL expiration
- Snapshot/load to disk
- CLI tool and benchmarks

### 🚀 Quickstart

```bash
python cli/main.py add --id doc1 --vector 0.1 0.2 0.3
python cli/main.py search --vector 0.1 0.2 0.3 --topk 3
