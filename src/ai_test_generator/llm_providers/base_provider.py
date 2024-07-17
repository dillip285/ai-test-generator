from abc import ABC, abstractmethod

class BaseLLMProvider(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass

    @abstractmethod
    def generate_test_plan(self, code_analysis: str) -> str:
        pass
