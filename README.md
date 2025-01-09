# BICAN Knowledgebase Data Models

This repo contains data models generated using [LinkML](https://linkml.io/linkml/) for the [BICAN knowledgebase project](https://www.portal.brain-bican.org/teams/bican-knowledgebase) founded by the National Institute of Mental Health.


## Status Board

Here are the BICAN LinkML knowledgebase schemas and their statuses.

| Model                                                                                                                      | Short Description                                                                                                          | Release with Latest Updates | Status |
|:---------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|:----------------------------|:--|
| [Assertion Evidence Model]                                                                                                 | Types and relationships of assertions and evidences/                                                                       | 0.2.0                       | under development |
| [Library Generation Model]                                                                                                 | Types and relationships of samples and digital data assets generated during processes that generate multimodal genomic data. | 0.2.0                       | under development |
| [Anatomical Structure Model]                                                                                               | Types and relationships of anatomical brain structures.                                                                    | 0.1.0                       | under development |
| [Genome Annotation Model]                                                                                                  | Types and relationships of an organism's annotated genome.                                                                 | 0.2.0                       | under development |
| [BICAN BioLink]                                                                                                            | BICAN subset of classes from the Biolink model.                                                                            | 0.2.0                       | under development |
| [CCN2]                                                                                                                     |                                                                                                                            | 0.1.0                       | deprecated |
| [Figure1]                                                                                                                  |                                                                                                                            | 0.1.0                       | deprecated | |                | |

[Assertion Evidence Model]: linkml-schema/assertion_evidence.yaml

[BICAN BioLink]: linkml-schema/bican_biolink.yaml

[CCN2]: linkml-schema/ccn2.yaml

[Genome Annotation Model]: linkml-schema/genome_annotation.yaml

[Library Generation Model]: linkml-schema/library_generation.yaml

[Anatomical Structure Model]: linkml-schema/anatomical_structure.yaml

[Figure1]: linkml-schema/figure1.yaml

## Structure of the Repository

### LinkML Schema

In this project we use the [LinkML](https://linkml.io/linkml/), the Linked Data Modeling Language, to define the data models.
LinkML is a flexible modeling language that allows you to author schemas in YAML format, and it is designed to be both human-readable and machine-readable.
LinkML framework provides also a set of tools to generate code in different languages, such as Python, JSON, and RDF, from the schema files.

All the LinkML schema files are stored in the `linkml-schema` directory. 
Some of the models are written directly in the YAML format, while others automatically generated from Google sheets using the LinkML tool [schemasheets](https://linkml.io/schemasheets/),
 and the `schema2model` tool from the [`bkbit` package](https://github.com/brain-bican/bkbit).
You can find the specific information in [linkml-schema/README.md](linkml-schema/README.md).

### Additional Formats

The LinkML schema files are used to generate additional formats, such as JSON Schema and Pydantic models.
All files are generated automatically using GitHub Actions workflow whenever the LinkML schema files are updated.
You can see the specific workflow in the [reusable workflow](.github/workflows/reusable-generate_other_formats.yaml) that is reused for all models.

Currently, we are supporting the following formats:
- [Pydantic models](models_py-autogen): these models are used in the [Brain Knowledge Base Interaction Toolkit (bkbit)](https://github.com/brain-bican/bkbit)
- [JSON Schema](json-schema-autogen)
- [JSON-LD Context](jsonld-context-autogen)
- [ER Diagrams](erdiagram-autogen)



### Validation
All the schemas are automatically tested in the GitHub Actions workflow 
using LinkML validation tools ([see test_lint.yaml for details](.github/workflows/tests_lint.yaml)) 
and Python API and pytest ([see test_models.yaml for details](.github/workflows/tests_models.yaml)).

In order to run the pytest test locally, you can use the following commands:
```python
pip install -e .[test]
pytest -vs
```

## Terms of Use

These materials are provided under the Attribution International 4.0 (CC-BY-4.0) license, which is available at https://creativecommons.org/licenses/by/4.0/

## Acknowledgements

An extensible brain knowledge base and toolset spanning modalities for multi-species data-driven cell types
BICAN Knowledgebase
National Institute of Mental Health
Award # 1U24MH130918-01
