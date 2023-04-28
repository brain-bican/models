# BICAN Knowledgebase data models

This repo contains data models generated using linkML for BICAN knowledgebase.
Gene annotation, genome annotation, and genome assembly models are currently represented in kbmodel. 
The existing models such as biolink and ccn are imported.

In `/linkml-schema`, there are linkML `yaml` schema files that adhere to the linkML version of `1.5.0`.

In `/json-schema` and `/models_py`, there are `json` and `py` files generated using linkML schema for e.g.:
* `gen-json-schema linkml-schema/kbmodel.yaml > json-schema/kbmodel.json`
* `gen-pydantic linkml-schema/kbmodel.yaml > models_py/kbmodel.py`

In `/data-examples`, there are source data files in csv format, as well as a translator script in `/utils` that maps the csv data to the current data model in `kbmodel`.
The way to run the script is as follows:
* `python3 -i data-examples/utils/translator.py`
This generates `data.yaml`.
The other data file `figure1exampledata.yaml` is representing relational data in figure 1 of `A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain`
* https://www.biorxiv.org/content/10.1101/2023.03.06.531121v1.full.pdf 

Notes:
Initialize the packages using:
* `python -m pip install .`
* `python -m pip install .[test]`

Run `pytest` to run all tests in `/tests`