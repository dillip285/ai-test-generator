from pathlib import Path
from .base_agent import BaseAgent
from ..llm_providers import get_llm_provider

class CodeAnalyzerAgent(BaseAgent):
    def __init__(self, config):
        super().__init__(config)
        self.llm = get_llm_provider(config, "code_analyzer")

    def execute(self, file_path: Path):
        with open(file_path, "r") as f:
            code_content = f.read()

        analysis_prompt = f"Analyze the following Python code and provide a summary of its structure, classes, functions, and potential test cases:\n\n{code_content}"
        return self.llm.generate_response(analysis_prompt)
