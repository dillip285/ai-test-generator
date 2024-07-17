from .pytest_framework import PytestFramework
from .unittest_framework import UnittestFramework

def get_test_framework(framework: str):
    framework = framework.lower()
    if framework == "pytest":
        return PytestFramework()
    elif framework == "unittest":
        return UnittestFramework()
    else:
        raise ValueError(f"Unsupported test framework: {framework}")
