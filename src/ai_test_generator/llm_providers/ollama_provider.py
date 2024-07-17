import requests
from .base_provider import BaseLLMProvider

class OllamaProvider(BaseLLMProvider):
    def __init__(self, config):
        super().__init__(config)
        self.model = config["model"]
        self.api_url = "http://localhost:11434/api/generate"

    def generate_response(self, prompt: str) -> str:
        response = requests.post(self.api_url, json={
            "model": self.model,
            "prompt": prompt
        })
        return response.json()["response"]

    def generate_test_plan(self, code_analysis: str) -> str:
        prompt = f"Based on the following code analysis, generate a test plan:\n\n{code_analysis}"
        return self.generate_response(prompt)
