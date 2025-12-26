# Week 4 Diagnostic Task

This folder contains the work for Week 4, focusing on Embeddings and Semantic Search.

## Level 1: Basic Embeddings
Located in `level1/`.
- **Goal:** Turn sentences into vectors and measure cosine similarity.
- **Key File:** `embeddings_basic.py`
- **Output:** `nearest_neighbours.txt` shows example sentences and their semantic matches.
- **Outcome:** successfully demonstrated that the model matches semantically similar sentences even if they share few words (e.g., "astronomers observed" vs "stargazers used optical instrument").

## Level 2: Tiny Semantic Search
Located in `level2/`.
- **Goal:** Build a small semantic search engine.
- **Key File:** `semantic_search.py`
- **Output:** `search_examples.txt` showing queries against a small corpus.
- **Outcome:** The system can answer natural language queries like "Who built the aqueducts?" by retrieving relevant paragraphs about Roman engineering, with retrieval times under 10ms.

## How to Run
1. Install dependencies: `uv pip install sentence-transformers`.
2. Run Level 1: `python level1/embeddings_basic.py`.
3. Run Level 2: `python level2/semantic_search.py` (interactive) or `python level2/semantic_search.py --demo`.
