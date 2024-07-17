import requests
from .base_provider import BaseLLMProvider

class GroqProvider(BaseLLMProvider):
    def __init__(self, config):
        super().__init__(config)
        self.api_key = config["api_key"]
        self.model = config["model"]
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"

    def generate_response(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1000,
            "temperature": 0.7
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()

    def generate_test_plan(self, code_analysis: str) -> str:
        prompt = f"Based on the following code analysis, generate a test plan:\n\n{code_analysis}"
        return self.generate_response(prompt)
