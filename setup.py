from setuptools import setup, find_packages
import os

def get_version():
    version = os.environ.get('GITHUB_REF_NAME')
    if version:
        return version.lstrip('v')
    return '0.0.0'  # default version

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
    print(long_description)

setup(
    name="ai-test-generator",
    version=get_version(),
    author=os.environ.get('GITHUB_AUTHOR_NAME', 'Unknown'),
    author_email=os.environ.get('GITHUB_AUTHOR_EMAIL', 'unknown@example.com'),
    description="AI-powered test case generator for Python projects",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
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
