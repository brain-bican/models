from pathlib import Path

from linkml.generators.pythongen import PythonGenerator

import pytest

TEST_DIR = Path(__file__).parent
MODEL_LISTS = [
    "ccn2.yaml",
    "figure1.yaml",
]

@pytest.mark.parametrize("model", MODEL_LISTS)
def test_python_generators(model):
    model_python = PythonGenerator(f"{TEST_DIR}/../{model}").serialize()

