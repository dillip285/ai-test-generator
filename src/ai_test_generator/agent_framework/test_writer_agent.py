from pathlib import Path
from .base_agent import BaseAgent
from ..llm_providers import get_llm_provider
from ..test_frameworks import get_test_framework

class TestWriterAgent(BaseAgent):
    def __init__(self, config):
        super().__init__(config)
        self.llm = get_llm_provider(config, "test_writer")

    def execute(self, file_path: Path, test_plan: str, framework: str):
        test_framework = get_test_framework(framework)

        test_code_prompt = f"Write Python test cases using the {framework} framework for the following test plan:\n\n{test_plan}"
        test_code = self.llm.generate_response(test_code_prompt)

        output_dir = Path(self.config["output_directory"])
        output_dir.mkdir(parents=True, exist_ok=True)

        test_file_path = output_dir / f"test_{file_path.name}"
        with open(test_file_path, "w") as f:
            f.write(test_framework.generate_imports())
            f.write("\n\n")
            f.write(test_code)

        print(f"Test file generated: {test_file_path}")
