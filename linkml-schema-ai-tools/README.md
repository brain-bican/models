# GFF3 LinkML Modeling Task

## Run 1 
### User Prompt
Task: create a linkml model 
Background: You are an expert in data modeling and the tool LinkML. 
Goal: Given the linkml-schema-ai-tools/gff3.md file, create a linkml model to represent the data present in a gff3 file. You can also import and use classes from the linkml-schema/bican_biolink.yaml and linkml-schema/bican_core.yaml linkml models.
### Model 
 - openai/gpt-5
### AI Summary of Task
Background
- Create a simple, interoperable LinkML schema to represent GFF3 (Generic Feature Format Version 3) data, following the official specification.

Goal
- Build a LinkML model that captures the data present in a GFF3 file, guided by linkml-schema-ai-tools/gff3.md.

Reuse
- The schema may import and reuse classes/slots from:
  - linkml-schema/bican_biolink.yaml (Biolink subset commonly used in BICAN)
  - linkml-schema/bican_core.yaml (BICAN core metadata such as versioning and checksums)

Scope and Requirements
- Represent all nine GFF3 columns: seqid, source, type, start, end, score, strand, phase, attributes.
- Support reserved attributes: ID, Name, Alias, Parent, Target, Gap, Derives_from, Note, Dbxref, Ontology_term, Is_circular.
- Allow additional (non-reserved) attributes starting with lowercase names.
- Model feature hierarchies and multi-line features (e.g., repeated IDs for discontinuous features).
- Include support for sequence region directives (##sequence-region) and optional FASTA sections (##FASTA).
- Constrain strand and phase via enums; enforce positive integer coordinates; allow SO terms/IDs in the type field.

Deliverable
- A LinkML YAML schema that adheres to the above (e.g., linkml-schema/gff3.yaml), suitable for generating downstream artifacts (e.g., Pydantic models) and validating GFF3-derived data.

## Run 2
### User Prompt
Task: create a linkml model 
Background: You are an expert in data modeling and the tool LinkML. 
Goal: Given the linkml-schema-ai-tools/gff3.md file, create a linkml model to represent the data present in a gff3 file. We are only interested in representing feature types that are 'genes' and the associated information stored in the 'attributes' column. 
Reuse: linkml-schema/bican_biolink.yaml (a biolink subset commonly used in BICAN) and linkml-schema/bican_core.yaml (BICAN core metadata such as versioning and checksums)
### Model 
 - openai/gpt-5

## Run 3
### User Prompt
Task: create a linkml model 
Background: You are an expert in data modeling and the tool LinkML. 
Goal: Given the 'linkml-schema-ai-tools/gff3.md' file, create a linkml model to represent the data present in a gff3 file. We are only interested in representing feature types that are 'genes' and the associated information stored in the 'attributes' column. 
Example Data: 'data/GCF_000003025.6_Sscrofa11.1_genomic.gff' is an example of how data is represented in a gff3 file. Use this file to help refine the model. 
Reuse: linkml-schema/bican_biolink.yaml (a biolink subset commonly used in BICAN) and linkml-schema/bican_core.yaml (BICAN core metadata such as versioning and checksums)
Testing: Test the generated linkml model by running 2 commands. First run : 'linkml lint' and then run 'linkml generate pydantic'.
### Model 
 - openai/gpt-5

## Run 4
### User Prompt
Task:
Design a LinkML schema that models the metadata of a GFF3 file, focusing specifically on gene-level features and their associated attributes.

Background:
You are an expert in data modeling and the LinkML framework. The goal is to capture the essential structure and semantics of gene features as represented in GFF3 files.

Inputs:
Use the following reference files to understand the GFF3 structure and attribute conventions:

linkml-schema-ai-tools/gff3.md — general GFF3 specification summary

linkml-schema-ai-tools/ncbi_gff3.txt —  documentation from NCBI GFF3 format

linkml-schema-ai-tools/ensembl_gff3.md —  documentation from Ensembl GFF3 format


Goal:

Create a LinkML schema that represents the GFF3 file structure, but only for features of type “gene”.

Model the core GFF3 columns (e.g., seqid, source, type, start, end, score, strand, phase) as appropriate.

Focus primarily on modeling the attributes column, unifying attribute definitions and types between NCBI and Ensembl conventions. For aunified attributes, also provide mapping to original attribute name from NCBI and Ensembl.

Include clear descriptions, slot ranges, and enums where applicable.

Reuse existing entities, mixins, and patterns from:

linkml-schema/bican_biolink.yaml — Biolink subset used in BICAN

linkml-schema/bican_core.yaml — Core BICAN metadata (e.g., versioning, provenance, checksums)

DO NOT READ FROM ANY OTHER FILES.

Deliverables:

A complete LinkML schema file (YAML) defining the GFF3Gene class (or similar), associated slots, and unified attribute representation. Place schema in a new file in the linkml-schema-ai-tools directory.

Include appropriate schema metadata (e.g., id, name, description, version, prefixes, imports).

Ensure semantic reuse of terms consistent with Biolink and BICAN naming conventions.

Testing:
After creating the schema, validate it by running the following commands:

linkml lint
linkml generate pydantic


Ensure both commands execute successfully without errors or warnings.
### Model 
 - openai/gpt-5