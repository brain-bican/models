# `LinkML` schemas for the BICAN project

This folder contains all the original LinkML schemas written in YAML format.
You can learn more about the LinkML language [here](https://linkml.io/linkml/).

Some of the models are written directly in the YAML format, while others automatically generated from Google sheets using the LinkML tool [schemasheets](https://linkml.io/schemasheets/),
 and the `schema2model` tool from the [`bkbit` package](https://github.com/brain-bican/bkbit).


## Main models

The list below contains the main models, that are exported to different formats, such as JSON Schema, Pydantic models, and JSON-LD context.
We also have some additional auxiliary models that are used to extract the core types and used by the main models.

### [anatomical_structure](anatomical_structure.yaml)
The Anatomical Structure schema is designed to represent types and relationships of anatomical brain structures. 

##### Updates
The model has been created directly in the YAML format, and all the updates can be done by editing the file directly.


### [assertion_evidence](assertion_evidence.yaml)
The Assertion Evidence schema is designed to represent types and relationships of assertions and evidences.

##### Updates
The model has been created from the Google sheet, all information of the Google sheet id and id of the specifics tabs
 are in the [setting file](source_assertion_evidence/gsheet.yaml). 
The [source_assertion_evidence/gsheet_output](source_assertion_evidence/gsheet_output) folder contains the _cvs_ files generated from the Google sheet 
at the time of the model creation.

### [genome_annotation](genome_annotation.yaml)
The Genome Annotation schema is designed to represent types and relationships of an organism's annotated genome.

##### Updates
The model has been created directly in the YAML format, and all the updates can be done by editing the file directly.

### [library_generation](library_generation.yaml)
The Library Generation schema is designed to represent types and relationships of samples and 
digital data assets generated during processes that generate multimodal genomic data.

##### Updates
The model has been created from the Google sheet, all information of the Google sheet id and id of the specifics tabs
 are in the [setting file](source_library_generation/gsheet.yaml). 
The [source_library_generation/gsheet_output](source_library_generation/gsheet_output) folder contains the _cvs_ files generated from the Google sheet 
at the time of the model creation.


## Auxiliary models

These models are used to extract the core types and used by the main models, you can see it in the `imports` sections.

### [anatomical_structure_core](anatomical_structure_core.yaml)

Contains the core types used in the [Anatomical Structure schema](anatomical_structure.yaml).

##### Updates
The model has been created directly in the YAML format, and all the updates can be done by editing the file directly.


### [bican_biolink](bican_biolink.yaml)
The model contains a subset of classes from the [Biolink model](https://biolink.github.io/biolink-model/)
with some small modification to fit the needs of the BICAN project (currently only the `category` slot is modified).

##### Updates

The yaml file can be recreated by running the [LinkML trimmer](https://github.com/brain-bican/bkbit/blob/main/bkbit/model_editors/README.md)
from `bkbit` package.:
```bash
TODO
```
In order to adjust the `category` slot, the following you can run:
```commandline
python ../utils/bican_biolink_edit.py bican_biolink.yaml
```

### [bican_core](bican_core.yaml)
The BICAN Core schema is designed to represent classes, slots, and enums that are frequently used in BICAN schemas.

##### Updates
The model has been created directly in the YAML format, and all the updates can be done by editing the file directly.

### [bican_prov](bican_prov.yaml)
The BICAN Prov schema contains a subset of classes from the Prov Data Model (PROV-DM) that are frequently used in BICAN schemas.

##### Updates
The model has been created directly in the YAML format, and all the updates can be done by editing the file directly.


## Deprecated models

These are models that are no longer used, but are kept for reference.

### [ccn2](ccn2.yaml)
A depreciated model, initial attempt to convert a CCN2 model to LinkML.

### [figure1](figure1.yaml)
A depreciated model, initial attempt to provide a schema for data presented on Figure1 from [Yao, Z. et al., _Nature_ 624 (2023)](https://www.nature.com/articles/s41586-023-06812-z#citeas).
