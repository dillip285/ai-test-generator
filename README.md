# AI Test Generator

AI Test Generator is a powerful CLI tool that leverages artificial intelligence to automatically generate test cases for Python projects. It uses a combination of AI agents and language models to analyze your code, plan test scenarios, and write detailed test cases.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [LLM Providers](#llm-providers)
- [Project Structure](#project-structure)
- [Implementation Details](#implementation-details)
- [Contributing](#contributing)
- [Changelog](#changelog)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Support](#support)

## Features

- Supports multiple AI providers (OpenAI, Ollama, Groq, Claude)
- Generates test cases for individual Python files or entire directories
- Configurable test frameworks (pytest, unittest)
- Customizable agent-to-LLM provider mapping
- Easy-to-use command-line interface

## Installation

You can install AI Test Generator using pip:

```bash
pip install ai-test-generator
```

## Usage
 ### Basic Usage

To generate test cases for a single Python file:
```bash
ai-test-generator generate path/to/your/file.py
```
To generate test cases for an entire directory:
```bash
ai-test-generator generate path/to/your/project/
```
Specifying Test Framework
You can specify the test framework you want to use (default is pytest):

```bash
Copyai-test-generator generate path/to/your/file.py --framework unittest
```

## Configuration
AI Test Generator can be configured using a YAML file named ai_test_generator_config.yaml in your project directory. Here's an example

```yaml configuration:
default_llm_provider: ollama
llm_providers:
  ollama:
    model: codellama
  openai:
    api_key: "your-openai-api-key-here"
    model: gpt-3.5-turbo
  groq:
    api_key: "your-groq-api-key-here"
    model: mixtral-8x7b-32768
  claude:
    api_key: "your-anthropic-api-key-here"
    model: claude-3-opus-20240229
output_directory: tests
agent_llm_mapping:
  planner: claude
  code_analyzer: ollama
  test_writer: groq
```
## Configuration Options

default_llm_provider: The default LLM provider to use if not specified for an agent.
llm_providers: Configuration for each supported LLM provider.

ollama: Local LLM provider (no API key required)
openai: OpenAI's GPT models
groq: Groq's API
claude: Anthropic's Claude AI


output_directory: The directory where generated test files will be saved.
agent_llm_mapping: Specify which LLM provider to use for each agent type.

## LLM Providers
### Ollama
Ollama is a local LLM provider that doesn't require an API key. Make sure you have Ollama installed and running on your system.
### OpenAI
To use OpenAI's models, you need to sign up for an API key at https://openai.com and add it to your configuration file.
### Groq
To use Groq's API, sign up for an API key at https://console.groq.com and add it to your configuration file.
### Claude
To use Anthropic's Claude AI, sign up for an API key at https://www.anthropic.com and add it to your configuration file.
## Project Structure

ai-test-generator/
├── pyproject.toml
├── README.md
├── LICENSE
├── MANIFEST.in
├── setup.py
├── src/
│   ├── ai_test_generator/
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   ├── config.py
│   │   ├── agent_framework/
│   │   │   ├── __init__.py
│   │   │   ├── base_agent.py
│   │   │   ├── planner_agent.py
│   │   │   ├── code_analyzer_agent.py
│   │   │   └── test_writer_agent.py
│   │   ├── llm_providers/
│   │   │   ├── __init__.py
│   │   │   ├── base_provider.py
│   │   │   ├── ollama_provider.py
│   │   │   ├── openai_provider.py
│   │   │   ├── groq_provider.py
│   │   │   └── claude_provider.py
│   │   └── test_frameworks/
│   │       ├── __init__.py
│   │       ├── pytest_framework.py
│   │       └── unittest_framework.py
│   └── tests/
│       ├── __init__.py
│       ├── test_cli.py
│       ├── test_config.py
│       └── test_agent_framework.py
└── example_config.yaml

## Implementation Details
### CLI (cli.py)
The CLI is implemented using the fire library, providing a simple interface for users to generate test cases.
### Configuration (config.py)
The configuration module handles loading and merging user-defined configurations with default settings.
### Agent Framework

- base_agent.py: Defines the base class for all agents.
- planner_agent.py: Orchestrates the test generation process.
- code_analyzer_agent.py: Analyzes the input Python code.
- test_writer_agent.py: Generates test cases based on the analysis.

### LLM Providers

- base_provider.py: Defines the interface for LLM providers.
- ollama_provider.py: Implements the Ollama LLM provider.
- openai_provider.py: Implements the OpenAI LLM provider.
- groq_provider.py: Implements the Groq LLM provider.
- claude_provider.py: Implements the Claude AI LLM provider.

### Test Frameworks

- pytest_framework.py: Handles pytest-specific test generation.
- unittest_framework.py: Handles unittest-specific test generation.

## Contributing
Contributions are welcome! Please follow these steps to contribute:

- Fork the repository
- Create a new branch: git checkout -b feature-branch-name
- Make your changes and commit them: git commit -m 'Add some feature'
- Push to the branch: git push origin feature-branch-name
- Submit a pull request

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## Changelog
** v0.1.0 (Initial Release) **

* Basic test generation functionality
* Support for multiple LLM providers (Ollama, OpenAI, Groq, Claude)
* Configurable agent-to-LLM mapping
* Support for pytest and unittest frameworks

License
This project is licensed under the MIT License - see the LICENSE file for details.
Disclaimer
This tool generates test cases based on AI analysis and may not cover all possible scenarios. It's recommended to review and supplement the generated tests with your own domain knowledge and edge cases.
Support
If you encounter any issues or have questions, please file an issue on the GitHub repository.

Happy testing with AI Test Generator! 🚀🤖
