import openai
from .base_provider import BaseLLMProvider

class OpenAIProvider(BaseLLMProvider):
    def __init__(self, config):
        super().__init__(config)
        openai.api_key = config["api_key"]
        self.model = config["model"]

    def generate_response(self, prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].message["content"].strip()

    def generate_test_plan(self, code_analysis: str) -> str:
        prompt = f"Based on the following code analysis, generate a test plan:\n\n{code_analysis}"
        return self.generate_response(prompt)
