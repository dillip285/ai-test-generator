from .ollama_provider import OllamaProvider
from .openai_provider import OpenAIProvider
from .groq_provider import GroqProvider
from .claude_provider import ClaudeProvider

LLM_PROVIDERS = {
    "ollama": OllamaProvider,
    "openai": OpenAIProvider,
    "groq": GroqProvider,
    "claude": ClaudeProvider
}

class LLMProviderManager:
    def __init__(self, config):
        self.config = config
        self.providers = {}

    def get_provider(self, provider_name=None):
        if provider_name is None:
            provider_name = self.config["default_llm_provider"]

        if provider_name not in self.providers:
            provider_class = LLM_PROVIDERS.get(provider_name)
            if provider_class is None:
                raise ValueError(f"Unsupported LLM provider: {provider_name}")
            provider_config = self.config["llm_providers"][provider_name]
            self.providers[provider_name] = provider_class(provider_config)

        return self.providers[provider_name]

def get_llm_provider(config, agent_type=None):
    manager = LLMProviderManager(config)
    if agent_type and agent_type in config["agent_llm_mapping"]:
        return manager.get_provider(config["agent_llm_mapping"][agent_type])
    return manager.get_provider()
