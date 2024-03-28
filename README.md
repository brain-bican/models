# BICAN Knowledgebase data models

This repo contains data models generated using [LinkML](https://linkml.io/linkml/) for BICAN knowledgebase. LinkML is a linked data modeling language that supports YAML, RDF, and JSON. 

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

## Status Board

Here are the BICAN LinkML knowledgebase schemas and their statuses.

| Model | Version | Release | Status |
|:--|:--|:--|:--|
| [BICAN BioLink] | [] |  [] | under development |
| [CCN2] | [] | [] | under development |
| [KB Model] | [] | [] | under development |
| [Library Generation Model] | [] | [] | under development |
| | | | |

[BICAN BioLink]: linkml-schema/bican_biolink.yaml

[CCN2]: linkml-schema/ccn2.yaml

[KB Model]: linkml-schema/kbmodel.yaml

[Library Generation Model]: linkml-schema/purple_boxes.yaml

## Contact

Satra Ghosh (PI -- MIT)

Lydia Ng (PI -- Allen Institute for Brain Science)

Puja Trivedi (MIT)

Dorota Jarecki (MIT)

Prajal Bishkawarma (Allen Institute for Brain Science)

Tim Fliss (Allen Insitute for Brain Science)

Pamela Baker (Allen Institute for Brain Science)

Patrick Ray (Allen Institute for Brain Science)

## Terms of Use

These materials are provided under the Attribution International 4.0 (CC-BY-4.0) license, which is available at https://creativecommons.org/licenses/by/4.0/

## Acknowledgements

An extensible brain knowledge base and toolset spanning modalities for multi-species data-driven cell types
BICAN Knowledgebase
National Institute of Mental Health
Award # 1U24MH130918-01