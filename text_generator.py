# text_generator.py / text_generator.ipynb
# -----------------------------------------
# Generative Text Model using GPT-2
# Generates coherent paragraphs on user-specified topics.

from transformers import pipeline, set_seed

# ---------- Step 1: Load pre-trained GPT-2 model ----------
generator = pipeline("text-generation", model="gpt2")

# ---------- Step 2: Take a user prompt ----------
topic = input("Enter a topic or prompt: ")

# ---------- Step 3: Generate text ----------
set_seed(42)  # for consistent results

result = generator(
    topic,
    max_length=150,         # total tokens (length of output)
    num_return_sequences=1, # number of paragraphs
    temperature=0.8,        # controls creativity (lower = more focused)
    top_p=0.9,              # nucleus sampling for coherence
)

# ---------- Step 4: Display result ----------
print("\nGenerated Text:\n")
print(result[0]['generated_text'])
