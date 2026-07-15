import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from llm.ollama_client import OllamaClient

client = OllamaClient()

embedding = client.embed(
    "Hello Nyrion AI"
)

print("Embedding dimension:", len(embedding))

reply = client.generate(
    "Say hello in one sentence."
)

print(reply)