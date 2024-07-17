import fire
from pathlib import Path
from ai_test_generator.config import load_config
from ai_test_generator.agent_framework.planner_agent import PlannerAgent

class AITestGenerator:
    def generate(self, file_path: str, framework: str = "pytest"):
        """Generate test cases for the given file or directory."""
        config = load_config()
        file_path = Path(file_path)

        if not file_path.exists():
            print(f"Error: {file_path} does not exist.")
            return

        planner = PlannerAgent(config)
        planner.plan_and_execute(file_path, framework)

def main():
    fire.Fire(AITestGenerator)

if __name__ == "__main__":
    main()
