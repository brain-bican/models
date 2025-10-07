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