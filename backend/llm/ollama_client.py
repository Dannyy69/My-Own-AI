import requests


class OllamaClient:

    def __init__(
        self,
        base_url="http://localhost:11434"
    ):
        self.base_url = base_url

    def embed(
        self,
        text,
        model="nomic-embed-text"
    ):

        response = requests.post(
            f"{self.base_url}/api/embed",
            json={
                "model": model,
                "input": text
            }
        )

        response.raise_for_status()

        data = response.json()

        if "embeddings" in data:
            return data["embeddings"][0]

        return data["embedding"]

    def generate(
        self,
        prompt,
        model="llama3.2"
    ):

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        return response.json()["response"]