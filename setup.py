from setuptools import setup, find_packages
import os

def get_version():
    version = os.environ.get('GITHUB_REF_NAME')
    if version:
        return version.lstrip('v')
    return '0.0.0'  # default version

# Read the contents of your README file
long_description = """
# AI Test Generator

AI Test Generator is a powerful CLI tool that leverages artificial intelligence to automatically generate test cases for Python projects. It uses a combination of AI agents and language models to analyze your code, plan test scenarios, and write detailed test cases.

## Features

- Supports multiple AI providers (OpenAI, Ollama, Groq, Claude)
- Generates test cases for individual Python files or entire directories
- Configurable test frameworks (pytest, unittest)
- Customizable agent-to-LLM provider mapping
- Easy-to-use command-line interface

## Installation

You can install AI Test Generator using pip:
pip install ai-test-generator

## Usage

To generate test cases for a single Python file:
ai-test-generator generate path/to/your/file.py

To generate test cases for an entire directory:
ai-test-generator generate path/to/your/project/

For more information and advanced usage, please refer to the project's GitHub repository.
"""

setup(
    name="ai-test-generator",
    version=get_version(),
    author=os.environ.get('GITHUB_AUTHOR_NAME', 'Unknown'),
    author_email=os.environ.get('GITHUB_AUTHOR_EMAIL', 'unknown@example.com'),
    description="AI-powered test case generator for Python projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dillip285/ai-test-generator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "fire>=0.5.0",
        "pyyaml>=6.0",
        "requests>=2.26.0",
        "openai>=1.1.0",
        "anthropic>=0.3.0",
    ],
    entry_points={
        "console_scripts": [
            "ai-test-generator=ai_test_generator.cli:main",
        ],
    },
)
