import anthropic
from .base_provider import BaseLLMProvider

class ClaudeProvider(BaseLLMProvider):
    def __init__(self, config):
        super().__init__(config)
        self.api_key = config["api_key"]
        self.model = config["model"]
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate_response(self, prompt: str) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            temperature=0.7,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text

    def generate_test_plan(self, code_analysis: str) -> str:
        prompt = f"Based on the following code analysis, generate a test plan:\n\n{code_analysis}"
        return self.generate_response(prompt)
