import time
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/paraphrase-MiniLM-L6-v2"

sentences = [
    "The astronomers observed a distant galaxy through the telescope.",      # 0
    "Stargazers used an optical instrument to view remote celestial bodies.", # 1 (Similar to 0)
    "The bank by the river is eroding.",                                      # 2
    "I need to go to the bank to deposit a check.",                           # 3 (Lexical overlap with 2, diff meaning)
    "The chef prepared a delicious meal.",                                    # 4
    "He cooked a tasty dinner.",                                              # 5 (Similar to 4)
    "The Jaguar sped down the highway.",                                      # 6
    "The jaguar stalked its prey in the jungle.",                             # 7 (Lexical overlap with 6, diff meaning)
    "Artificial intelligence is transforming the world.",                     # 8
    "Machine learning algorithms are changing society."                       # 9 (Similar to 8)
]

def main():
    print("Loading model...")
    model = SentenceTransformer(MODEL_NAME)
    
    print("Encoding sentences...")
    start_time = time.perf_counter()
    embeddings = model.encode(sentences, normalize_embeddings=True)
    duration = time.perf_counter() - start_time
    print(f"Encoded {len(sentences)} sentences in {duration:.4f}s")
    
    # Compute cosine similarity
    similarity = embeddings @ embeddings.T
    
    output_path = "level1/nearest_neighbours.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("=== LEVEL 1: EMBEDDINGS + NEAREST NEIGHBOURS ===\n")
        f.write(f"Encoded {len(sentences)} sentences in {duration:.4f}s\n\n")
        
        for i, sentence in enumerate(sentences):
            scores = similarity[i]
            # Get top 3 excluding self
            indexed_scores = [(idx, score) for idx, score in enumerate(scores) if idx != i]
            indexed_scores.sort(key=lambda x: x[1], reverse=True)
            top_3 = indexed_scores[:3]
            
            f.write(f"[{i}] {sentence}\n")
            print(f"[{i}] {sentence}")
            for rank, (idx, score) in enumerate(top_3):
                line = f"  {rank+1}. [{idx}] (Score: {score:.4f}) {sentences[idx]}\n"
                f.write(line)
                print(line.strip())
            f.write("\n")
            print()
            
        # Analysis Notes
        f.write("=== ANALYSIS NOTES ===\n")
        f.write("1. Lexically different but semantically close:\n")
        f.write("   - Sentences [0] and [1]: 'astronomers observed' vs 'Stargazers used an optical instrument'.\n")
        f.write("     Different words, but high cosine similarity because the meaning is almost identical.\n\n")
        f.write("2. Lexically similar but semantically far apart:\n")
        f.write("   - Sentences [6] and [7]: 'The Jaguar' (car) vs 'The jaguar' (animal).\n")
        f.write("     High lexical overlap ('Jaguar', 'The') but the context differentiates them (highway vs jungle).\n")
        f.write("     Ideally, the model should separate them, though similarity might still be moderate due to shared words.\n")
    
    print(f"Output written to {output_path}")

if __name__ == "__main__":
    main()
