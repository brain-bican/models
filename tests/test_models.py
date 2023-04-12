from pathlib import Path

from linkml.utils.schemaloader import SchemaLoader

import pytest

TEST_DIR = Path(__file__).parent
MODEL_LISTS = [
    "ccn2.yaml",
    "figure1.yaml",
]

@pytest.mark.parametrize("model", MODEL_LISTS)
def test_models(model):
    """Checking if the models are valid linkml schmeas"""
    schema = SchemaLoader(f"{TEST_DIR}/../{model}")
    schema.resolve()

