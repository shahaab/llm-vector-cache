from setuptools import setup, find_packages

setup(
    name="llm_vector_cache",
    version="0.1.0",
    description="In-memory vector cache for LLM embeddings with similarity search, LRU, and TTL.",
    author="Shahaab",
    author_email="mshahaabmanzar@example.com",
    packages=find_packages(where="."),  # discovers engine, cli, etc.
    install_requires=[
        "numpy>=1.24",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "vector-cache=cli.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
