from pathlib import Path

from linkml.utils.schemaloader import SchemaLoader

import pytest

MODEL_LISTS = (Path(__file__).parent / "../linkml-schema").glob("*.yaml")

@pytest.mark.parametrize("model", MODEL_LISTS)
def test_models(model):
    """Checking if the models are valid linkml schmeas"""
    schema = SchemaLoader(str(model))
    schema.resolve()

