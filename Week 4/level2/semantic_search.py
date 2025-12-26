import time
import argparse
import sys
import numpy as np
from sentence_transformers import SentenceTransformer

# --- CORPUS DEFINITION ---
corpus = [
    # Ancient Rome
    "The Roman Empire was one of the largest empires in ancient history.",
    "Roman engineering brought us aqueducts, roads, and concrete.",
    "The Colosseum hosted gladiatorial games and public spectacles.",
    "Julius Caesar was a Roman general and statesman who played a critical role in the events that led to the demise of the Roman Republic.",
    "The eruption of Mount Vesuvius in 79 AD buried the Roman city of Pompeii.",
    "Roman law forms the basic framework for civil law systems in many countries today.",
    
    # Quantum Mechanics
    "Quantum mechanics is a fundamental theory in physics that describes the physical properties of nature at the scale of atoms and subatomic particles.",
    "The uncertainty principle asserts a fundamental limit to the precision with which certain pairs of physical properties can be known.",
    "Schrödinger's cat is a thought experiment that illustrates the paradox of quantum superposition.",
    "Quantum entanglement occurs when particles interact in ways such that the quantum state of each particle cannot be described independently.",
    "Wave-particle duality posits that every particle or quantum entity may be described as either a particle or a wave.",
    "Quantum computing aims to use quantum phenomena to perform computation.",
    
    # Sourdough Bread
    "Sourdough bread is made by the fermentation of dough using naturally occurring lactobacilli and yeast.",
    "A sourdough starter is a stable culture of yeast and lactic acid bacteria in a flour and water mixture.",
    "Long fermentation times allow for better gluten structure and flavor development in the bread.",
    "Scoring the dough before baking controls how the bread expands in the oven.",
    "Steam in the oven helps create a crispy crust on the bread.",
    "Whole wheat flour contains more nutrients and fiber than white flour.",
    
    # Machine Learning
    "Machine learning is a field of inquiry devoted to understanding and building methods that 'learn'.",
    "Supervised learning involves training a model on labeled data.",
    "Neural networks are computing systems inspired by the biological neural networks that constitute animal brains.",
    "Deep learning uses multi-layered neural networks to learn representations of data.",
    "Overfitting happens when a model learns the training data too well, capturing noise.",
    "Natural language processing gives computers the ability to understand text and spoken words."
]

MODEL_NAME = "sentence-transformers/paraphrase-MiniLM-L6-v2"

def main():
    parser = argparse.ArgumentParser(description="Tiny Semantic Search Engine")
    parser.add_argument("--demo", action="store_true", help="Run demo queries automatically")
    args = parser.parse_args()

    print(f"Loading model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)
    
    print(f"Embedding corpus of {len(corpus)} documents...")
    start_time = time.perf_counter()
    corpus_embeddings = model.encode(corpus, normalize_embeddings=True)
    embed_time = time.perf_counter() - start_time
    print(f"Embedding time: {embed_time:.4f}s")
    
    demo_queries = [
        "Who built the aqueducts?",
        "How includes a starter work?",
        "What is superposition?",
        "Give me an explanation of neural nets.",
        "Can computers understand human speech?"
    ]
    
    if args.demo:
        print("\n=== RUNNING DEMO QUERIES ===")
        queries_to_run = demo_queries
    else:
        print("\n=== INTERACTIVE MODE (type 'exit' to quit) ===")
        queries_to_run = None

    while True:
        if args.demo:
            if not queries_to_run:
                break
            query = queries_to_run.pop(0)
            print(f"\nQuery: {query}")
        else:
            try:
                query = input("\nEnter query: ").strip()
                if query.lower() in ("exit", "quit"):
                    break
                if not query:
                    continue
            except EOFError:
                break
        
        # Search
        t0 = time.perf_counter()
        query_embedding = model.encode(query, normalize_embeddings=True)
        
        # Cosine similarity
        scores = corpus_embeddings @ query_embedding.T
        
        # Top 3
        top_k_indices = np.argsort(scores)[::-1][:3]
        search_time = time.perf_counter() - t0
        
        print(f"Search time: {search_time:.4f}s")
        for rank, idx in enumerate(top_k_indices):
            print(f"  #{rank+1} (Score: {scores[idx]:.4f}) {corpus[idx]}")

if __name__ == "__main__":
    main()
