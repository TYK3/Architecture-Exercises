"""
DIAGNOSTIC TASK - Complete as many levels as you can

LEVEL 1: Get this working (required)
LEVEL 2: Expand it (tests Python skills)
LEVEL 3: Pick a challenge (tests thinking)
LEVEL 4: Build something new (tests creativity)

DUE: Wednesday 11:59 PM
Submit via: GitHub PR (preferred) or Teams #architecture channel.
See submission_format.txt for details.
"""

from transformers import pipeline
import time
import sys
import re

# Fix for Windows console encoding
sys.stdout.reconfigure(encoding='utf-8')

# LEVEL 1: Basic generation
print("=== LEVEL 1: BASIC GENERATION ===")
generator = pipeline('text-generation', model='distilgpt2')

prompts = [
    "The future of AI is",
    "In the year 2030",
    "The secret to happiness is"
]

for prompt in prompts:
    output = generator(prompt, max_length=30)
    print(f"\nPrompt: {prompt}")
    cleaned_output = re.sub(r'\n{3,}', '\n\n', output[0]['generated_text'].strip())
    print(f"Generated: {cleaned_output}")
    print("-" * 50)

# LEVEL 2: Experiments with parameters, timing, and saving to a file

print("\n=== LEVEL 2: EXPERIMENTS ===")

# Prompts specifically for Level 2 experiments
level2_prompts = [
    "AI will change education by",
    "In 20 years, most jobs will",
    "The ideal morning routine starts with",
    "The biggest challenge in robotics is",
    "In the future, cities will"
]

parameter_settings = [
    {"max_length": 40, "temperature": 0.7, "top_k": 50},
    {"max_length": 60, "temperature": 1.0, "top_k": 50},
    {"max_length": 60, "temperature": 1.2, "top_k": 100},
]

output_filename = "level2_results.txt"

# Open the file once and write everything into it
with open(output_filename, "w", encoding="utf-8") as f:
    f.write("LEVEL 2 RESULTS\n")
    f.write("================\n\n")

    # Loop over each prompt and each parameter setting
    for prompt in level2_prompts:
        for params in parameter_settings:
            # Time how long generation takes
            start_time = time.time()
            result = generator(
                prompt,
                max_length=params["max_length"],
                temperature=params["temperature"],
                top_k=params["top_k"],
                num_return_sequences=1,
                truncation=True,        # to avoid very long outputs if needed
            )
            elapsed = time.time() - start_time

            generated_text = result[0]["generated_text"]

            # Clean up the text: remove leading/trailing whitespace and collapse multiple newlines
            cleaned_text = generated_text.strip()
            cleaned_text = re.sub(r'\n{3,}', '\n\n', cleaned_text)

            # Count tokens in the generated text
            token_ids = generator.tokenizer.encode(generated_text)
            num_tokens = len(token_ids)

            # ---- Print to terminal ----
            print("\n--- LEVEL 2 RUN ---")
            print(f"Prompt: {prompt!r}")
            print(
                f"max_length={params['max_length']}, "
                f"temperature={params['temperature']}, "
                f"top_k={params['top_k']}"
            )
            print(f"Time taken: {elapsed:.3f} seconds")
            print(f"Token count: {num_tokens}")
            print("Generated text:")
            print(cleaned_text)
            print("-" * 50)

            # ---- Save the same information into the file ----
            f.write("--- LEVEL 2 RUN ---\n")
            f.write(f"Prompt: {prompt!r}\n")
            f.write(
                f"max_length={params['max_length']}, "
                f"temperature={params['temperature']}, "
                f"top_k={params['top_k']}\n"
            )
            f.write(f"Time taken: {elapsed:.3f} seconds\n")
            f.write(f"Token count: {num_tokens}\n")
            f.write("Generated text:\n")
"""
DIAGNOSTIC TASK - Complete as many levels as you can

LEVEL 1: Get this working (required)
LEVEL 2: Expand it (tests Python skills)
LEVEL 3: Pick a challenge (tests thinking)
LEVEL 4: Build something new (tests creativity)

DUE: Wednesday 11:59 PM
Submit via: GitHub PR (preferred) or Teams #architecture channel.
See submission_format.txt for details.
"""

from transformers import pipeline
import time
import sys
import re

# Fix for Windows console encoding
sys.stdout.reconfigure(encoding='utf-8')

# LEVEL 1: Basic generation
print("=== LEVEL 1: BASIC GENERATION ===")
generator = pipeline('text-generation', model='distilgpt2')

prompts = [
    "The future of AI is",
    "In the year 2030",
    "The secret to happiness is"
]

for prompt in prompts:
    output = generator(prompt, max_length=30)
    print(f"\nPrompt: {prompt}")
    cleaned_output = re.sub(r'\n{3,}', '\n\n', output[0]['generated_text'].strip())
    print(f"Generated: {cleaned_output}")
    print("-" * 50)

# LEVEL 2: Experiments with parameters, timing, and saving to a file

print("\n=== LEVEL 2: EXPERIMENTS ===")

# Prompts specifically for Level 2 experiments
level2_prompts = [
    "AI will change education by",
    "In 20 years, most jobs will",
    "The ideal morning routine starts with",
    "The biggest challenge in robotics is",
    "In the future, cities will"
]

parameter_settings = [
    {"max_length": 40, "temperature": 0.7, "top_k": 50},
    {"max_length": 60, "temperature": 1.0, "top_k": 50},
    {"max_length": 60, "temperature": 1.2, "top_k": 100},
]

output_filename = "level2_results.txt"

# Open the file once and write everything into it
with open(output_filename, "w", encoding="utf-8") as f:
    f.write("LEVEL 2 RESULTS\n")
    f.write("================\n\n")

    # Loop over each prompt and each parameter setting
    for prompt in level2_prompts:
        for params in parameter_settings:
            # Time how long generation takes
            start_time = time.time()
            result = generator(
                prompt,
                max_length=params["max_length"],
                temperature=params["temperature"],
                top_k=params["top_k"],
                num_return_sequences=1,
                truncation=True,        # to avoid very long outputs if needed
            )
            elapsed = time.time() - start_time

            generated_text = result[0]["generated_text"]

            # Clean up the text: remove leading/trailing whitespace and collapse multiple newlines
            cleaned_text = generated_text.strip()
            cleaned_text = re.sub(r'\n{3,}', '\n\n', cleaned_text)

            # Count tokens in the generated text
            token_ids = generator.tokenizer.encode(generated_text)
            num_tokens = len(token_ids)

            # ---- Print to terminal ----
            print("\n--- LEVEL 2 RUN ---")
            print(f"Prompt: {prompt!r}")
            print(
                f"max_length={params['max_length']}, "
                f"temperature={params['temperature']}, "
                f"top_k={params['top_k']}"
            )
            print(f"Time taken: {elapsed:.3f} seconds")
            print(f"Token count: {num_tokens}")
            print("Generated text:")
            print(cleaned_text)
            print("-" * 50)

            # ---- Save the same information into the file ----
            f.write("--- LEVEL 2 RUN ---\n")
            f.write(f"Prompt: {prompt!r}\n")
            f.write(
                f"max_length={params['max_length']}, "
                f"temperature={params['temperature']}, "
                f"top_k={params['top_k']}\n"
            )
            f.write(f"Time taken: {elapsed:.3f} seconds\n")
            f.write(f"Token count: {num_tokens}\n")
            f.write("Generated text:\n")
            f.write(cleaned_text + "\n")
            f.write("-" * 50 + "\n\n")

print(f"\nLevel 2 finished. Results saved to {output_filename}")


# LEVEL 3: Option B - Measure Quality
# I decided to build a simple scoring system to judge how "good" the text is.
# It looks at length, variety of words, and if it repeats itself too much.

def calculate_quality_score(text):
    """
    Gives a score from 0 to 100 based on simple heuristics.
    """
    score = 100
    
    # 1. Length check: If it's too short, it's probably not very interesting.
    if len(text) < 50:
        score -= 20
        # print("Penalty: Too short")
    
    # 2. Repetition check: If the same phrase appears too often, that's bad.
    # This is a simple check for repeated 4-word phrases.
    words = text.split()
    if len(words) > 4:
        phrases = set()
        repeats = 0
        for i in range(len(words) - 3):
            phrase = " ".join(words[i:i+4])
            if phrase in phrases:
                repeats += 1
            phrases.add(phrase)
        
        if repeats > 0:
            score -= (repeats * 10) # Big penalty for repetition!
            # print(f"Penalty: {repeats} repeated phrases")

    # 3. Vocabulary variety: Are we using different words?
    unique_words = set(word.lower() for word in words)
    if len(words) > 0:
        diversity_ratio = len(unique_words) / len(words)
        if diversity_ratio < 0.5: # If less than half the words are unique
            score -= 20
            # print("Penalty: Low vocabulary diversity")

    # Ensure score stays within 0-100
    return max(0, min(score, 100))

print("\n=== LEVEL 3: QUALITY SCORING (OPTION B) ===")
print("Testing the model with my new quality scorer...\n")

test_prompts = [
    "The best way to learn coding is",
    "Artificial intelligence will",
    "My favorite hobby is",
    "The weather today is",
    "Space exploration is important because",
    "In the future, cars will",
    "The history of the internet starts with",
    "To bake a cake, you need",
    "The funniest joke I know is",
    "Climate change requires"
]

# Let's run it on 10 prompts and see how it does!
for i, prompt in enumerate(test_prompts):
    # Generate text
    output = generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
    
    # Clean it up a bit first (using the fix from Level 2)
    cleaned_text = output.strip()
    else:
        print("Verdict: Needs improvement. 😕")
    print("-" * 30)

# LEVEL 4: Your code here
# TODO: Build something new
# TODO: Build something new