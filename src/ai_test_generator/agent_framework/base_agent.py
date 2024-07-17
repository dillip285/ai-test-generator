from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
