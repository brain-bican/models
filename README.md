# BICAN Knowledgebase Data Models

This repo contains data models generated using [LinkML](https://linkml.io/linkml/) for BICAN knowledgebase. LinkML is a linked data modeling language that supports YAML, RDF, and JSON. 

In `/linkml-schema`, there are linkML `yaml` schema files that adhere to the linkML version of `1.5.0`.
* The __Library Generation Model__ is designed to represent types and relationships of samples and digital data assets generated during processes that generate multimodal genomic data.
* The __Genome Annotation Model__ is designed to represent types and relationships of an organism's annotated genome i.e. gene annotations, genome annotations, genome assemblies, organisms.
* The __Anatomical Strucutre Model__ is designed to represent types and relationships of anatomical brain structures.
* The existing models such as __Biolink__  and __CCN__ are imported.

In `/json-schema` and `/models_py`, there are `json` and `py` files generated using linkML schema for e.g.:
* `gen-json-schema linkml-schema/genome_annotation.yaml > json-schema/genome_annotation.json`
* `gen-pydantic linkml-schema/genome_annotation.yaml > models_py/genome_annotation.py`

In `/data-examples`, there are source data files:
* `figure1exampledata.yaml` is representing relational data in figure 1 of `A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain`
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
| [Library Generation Model] | [] | [] | under development |
| [Anatomical Structure Model] | [] | [] | under development |
| [Genome Annotation Model] | [] | [] | under development |
| [BICAN BioLink] | [] |  [] | under development |
| [CCN2] | [] | [] | deprecated |
| [Figure1] | [] | [] | deprecated |
| | | | |

[BICAN BioLink]: linkml-schema/bican_biolink.yaml

[CCN2]: linkml-schema/ccn2.yaml

[Genome Annotation Model]: linkml-schema/genome_annotation.yaml

[Library Generation Model]: linkml-schema/library_generation.yaml

[Anatomical Structure Model]: linkml-schema/anatomical_structure.yaml

[Figure1]: linkml-schema/figure1.yaml

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