from pathlib import Path

from linkml.generators.pythongen import PythonGenerator

import pytest

MODEL_LISTS = (Path(__file__).parent / "../linkml-schema").glob("*.yaml")


@pytest.mark.parametrize("model", MODEL_LISTS)
@pytest.mark.xfail(reason="lack of support for curie in python generator, see issue #2436")
def test_python_generators(model):
    model_python = PythonGenerator(str(model)).serialize()

