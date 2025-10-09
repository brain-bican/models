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

 ## Run 5
### User Prompt
Task: Design a LinkML schema that models gene annotations derived from GFF3 gene features and organizes them into a reusable “genome annotation” package. The schema should:

1. Represent individual genes (derived from GFF3 rows where type=gene)
2. Represent a genome annotation dataset that the genes are referenced from
3. Represent the reference genome assembly used by the dataset
4. Provide a top-level collection to hold multiple gene annotations, genome annotations, and assemblies

Background: You are an expert in data modeling and the LinkML framework. The goal is to capture the essential structure and semantics of gene features from GFF3, while structuring the schema into a gene record class that references a dataset class (the genome annotation) with assembly context and minimal, clear controlled vocabularies.

Inputs: Use ONLY the following reference files to understand GFF3 structure and attribute conventions:

- linkml-schema-ai-tools/gff3.md — general GFF3 specification summary
- linkml-schema-ai-tools/ncbi_gff3.txt — documentation from NCBI GFF3 format
- linkml-schema-ai-tools/ensembl_gff3.md — documentation from Ensembl GFF3 format

Goal and required structure:

- Provide the following classes and relationships:

  1. GeneAnnotation (is_a: gene)

     - Represents a single gene derived from a GFF3 row with type=gene.
     - Must include: a small set of unifying attributes from GFF3’s attributes column, minimal biotype-like classification, and an explicit reference to the genome annotation dataset it came from.
     - Should include gene identity and optional location context; coordinates are allowed but keep them minimal and gene-appropriate.

  2. GenomeAnnotation (is_a: genome)

     - Represents a genome annotation dataset (e.g., an authority’s release of gene annotations).
     - Must include dataset-level metadata such as version, digest, content_url, and authority.
     - Must reference a genome assembly.

  3. GenomeAssembly (is_a: named thing; mixin: thing with taxon)

     - Represents the genome assembly used by the genome annotation.
     - Include minimal assembly metadata (e.g., version, strain).

  4. AnnotationCollection (tree_root: true)

     - A root container class for transporting sets of GeneAnnotation, GenomeAnnotation, and GenomeAssembly instances.
     - Provide list attributes for each of these item types, using inlined_as_list: true.

Class details:

1. GeneAnnotation (is_a: gene)

- Core identity and provenance:

  - slots: source_id, molecular_type
  - attributes:
    - referenced_in: required, inlined, any_of: [GenomeAnnotation, string] (the genome annotation dataset this gene came from)

- GFF3 gene columns (keep minimal and appropriate for “gene”):

  - seqid, source, type (constrain to “gene”), start, end, score, strand
  - Do NOT include “phase” for the gene feature (phase is for CDS)
  - Use a one-based integer type for start and end

- Unified attributes (Column 9 harmonization across NCBI/Ensembl):

  - molecular_type: any_of: [BioType, string] with small controlled vocabulary (see enums)

  - source_id: schema:identifier for the authority-specific identifier for this gene

  - Optional harmonized attributes with annotations for original provenance:

    - ensembl_gene_id (annotations: ensembl_attr: gene_id)
    - ncbi_gene_id (range: uriorcurie; annotations: ncbi_attr: Dbxref(GeneID))
    - biotype or a richer “gene_biotype” value (if provided), but map/roll-up to molecular_type for a simple classification
    - symbol, name, description, synonym, xref, version
    - locus_tag, pseudo (boolean), pseudogene_subtype, note

  - Provide slot_usage with exact_mappings/narrow_mappings to GFF3 attributes where applicable (e.g., ID, Name, Alias, Dbxref) and to the GFF3 columns (seqid, source, type, start, end, score, strand).

- Constraints:

  - type should be constrained to “gene” via an enum (e.g., GeneFeatureType with permissible value “gene”)
  - start/end should use a custom integer type with minimum_value: 1

2. GenomeAnnotation (is_a: genome)

- Dataset-level metadata:
  - slots: version, digest, content_url, authority
- Link to assembly:
  - attributes:
    - reference_assembly: required, inlined, any_of: [GenomeAssembly, string]
- Authority should be controlled by a small enum (e.g., AuthorityType with ENSEMBL, NCBI)

3. GenomeAssembly (is_a: named thing; mixins: [thing with taxon])

- slots: version, strain
- The mixin ensures taxon context is available for the assembly

4. AnnotationCollection (tree_root: true)

- attributes:

  - annotations: multivalued, inlined_as_list: true, range: GeneAnnotation
  - genome_annotations: multivalued, inlined_as_list: true, range: GenomeAnnotation
  - genome_assemblies: multivalued, inlined_as_list: true, range: GenomeAssembly

Slots to define (non-exhaustive; use clear descriptions and ranges):

- seqid (maps to GFF3 Column 1; consider accession.version semantics)
- source (GFF3 Column 2)
- type (GFF3 Column 3; constrained to gene)
- start (GFF3 Column 4; range: one_based_int with minimum_value: 1)
- end (GFF3 Column 5; range: one_based_int with minimum_value: 1)
- score (GFF3 Column 6; range: float)
- strand (GFF3 Column 7; use StrandEnum with +, -, ., ?)
- molecular_type (any_of: [BioType, string])
- authority (range: AuthorityType)
- source_id (slot_uri: schema:identifier)
- strain (string)
- referenced_in (as described above)
- reference_assembly (as described above)

Types:

- one_based_int: typeof: integer; minimum_value: 1

Enums:

- StrandEnum: +, -, ., ?
- GeneFeatureType: permissible value: gene
- BioType: permissible values: protein_coding, noncoding (keep intentionally small and simple)
- AuthorityType: permissible values: ENSEMBL, NCBI

Prefixes and imports:

- prefixes: linkml, bican, schema, NCBIGene, NCBIAssembly, NCBITaxon (add others as needed for GFF3 or Ensembl identifiers)
- imports: linkml:types, bican_biolink, bican_core
- default_prefix: bican
- default_range: string

Attribute harmonization guidance:

- For each unifying gene attribute, add annotations indicating original source keys (e.g., ncbi_attr: gene_biotype; ensembl_attr: biotype).
- For identifiers, ensure ncbi_gene_id is uriorcurie (e.g., NCBIGene:####) and ensembl_gene_id is a string (e.g., ENSG..., ENSMUSG...).
- Use exact_mappings or narrow_mappings to GFF3 keys (e.g., gff3:ID, gff3:Name, gff3:Dbxref) for clarity.

Deliverables:

- A single LinkML YAML file placed in linkml-schema-ai-tools defining:

  - The classes: GeneAnnotation, GenomeAnnotation, GenomeAssembly, AnnotationCollection
  - The slots, types, and enums listed above
  - Clear descriptions for classes/slots and mapping annotations to GFF3

- Include top-level schema metadata (id, name, description, version, prefixes, imports)

- Ensure semantic reuse of terms consistent with Biolink/BICAN naming where appropriate

Testing:

- Run:

  - linkml lint
  - linkml generate pydantic

- Both commands must execute successfully without errors or warnings.

Constraints:

- DO NOT READ FROM ANY OTHER FILES beyond the three Inputs specified above.

### Model 
 - openai/gpt-5