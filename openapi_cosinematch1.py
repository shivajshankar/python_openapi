import os
import openai
import numpy as np
from scipy.spatial.distance import cosine

# Make sure to set your OpenAI API key as an environment variable
# os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
openai.api_key = os.getenv("OPENAI_KEY")

def get_embedding(text):
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    embedding = response['data'][0]['embedding']
    return np.array(embedding)

def cosine_similarity(vec1, vec2):
    return 1 - cosine(vec1, vec2)

def compare_strings(string1, string2, threshold=0.8):
    embedding1 = get_embedding(string1)
    embedding2 = get_embedding(string2)

    similarity = cosine_similarity(embedding1, embedding2)

    print(f"Cosine Similarity: {similarity:.4f}")
    if similarity > threshold:
        print("The strings are similar.")
    else:
        print("The strings are not similar.")

if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    threshold = float(input("Enter the similarity threshold (e.g., 0.8): "))

    compare_strings(string1, string2, threshold)
