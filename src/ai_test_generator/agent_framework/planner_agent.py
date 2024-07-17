from pathlib import Path
from .base_agent import BaseAgent
from .code_analyzer_agent import CodeAnalyzerAgent
from .test_writer_agent import TestWriterAgent
from ..llm_providers import get_llm_provider

class PlannerAgent(BaseAgent):
    def __init__(self, config):
        super().__init__(config)
        self.llm = get_llm_provider(config, "planner")

    def plan_and_execute(self, file_path: Path, framework: str):
        if file_path.is_file():
            self._process_file(file_path, framework)
        elif file_path.is_dir():
            self._process_directory(file_path, framework)
        else:
            print(f"Error: {file_path} is neither a file nor a directory.")

    def _process_file(self, file_path: Path, framework: str):
        analyzer = CodeAnalyzerAgent(self.config)
        code_analysis = analyzer.execute(file_path)

        test_plan = self.llm.generate_test_plan(code_analysis)

        writer = TestWriterAgent(self.config)
        writer.execute(file_path, test_plan, framework)

    def _process_directory(self, directory: Path, framework: str):
        for file_path in directory.rglob("*.py"):
            if not file_path.name.startswith("test_"):
                self._process_file(file_path, framework)
