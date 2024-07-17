import yaml
from pathlib import Path

DEFAULT_CONFIG = {
    "default_llm_provider": "ollama",
    "llm_providers": {
        "ollama": {
            "model": "codellama"
        },
        "openai": {
            "api_key": "",
            "model": "gpt-3.5-turbo"
        },
        "groq": {
            "api_key": "",
            "model": "mixtral-8x7b-32768"
        },
        "claude": {
            "api_key": "",
            "model": "claude-3-opus-20240229"
        }
    },
    "output_directory": "tests",
    "agent_llm_mapping": {
        "planner": "openai",
        "code_analyzer": "ollama",
        "test_writer": "openai"
    }
}

def load_config():
    config_path = Path("ai_test_generator_config.yaml")
    if config_path.exists():
        with open(config_path, "r") as f:
            user_config = yaml.safe_load(f)
        return merge_configs(DEFAULT_CONFIG, user_config)
    return DEFAULT_CONFIG

def merge_configs(default_config, user_config):
    merged = default_config.copy()
    for key, value in user_config.items():
        if isinstance(value, dict) and key in merged:
            merged[key] = merge_configs(merged[key], value)
        else:
            merged[key] = value
    return merged
