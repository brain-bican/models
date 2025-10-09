# Evaluation Plan
## Prompt
task: compare linkml-schema-ai-tools/gff3_gene.yaml with linkmlml-schema/genome_annotation.yaml. Provide a similarity score as well as a summary where the 2 files are similar and where they are different

### Run 4 
Similarity score: 0.48 (48%)

Method (brief):
- Computed a composite score by comparing:
  - Imports and defaults (same LinkML foundations, weight 0.2; score 1.0)
  - Prefixes (Jaccard over declared prefixes, weight 0.15; score ≈0.40)
  - Conceptual class families (both define a gene entity and a dataset/container context, weight 0.2; score ≈0.75)
  - Explicit slot/attribute names used across classes (Jaccard over names used, weight 0.35; score ≈0.083; overlap: version, digest, content_url)
  - Enum concepts (biotype-like concept present in both, weight 0.1; score ≈0.5)
- Weighted sum ≈ 0.489 → 0.48.

Where they are similar:
- Foundations:
  - Both are LinkML schemas, default_prefix=bican, default_range=string.
  - Both import linkml:types, bican_biolink, bican_core.
  - Share common prefixes (linkml, bican, schema, NCBIGene).
- Conceptual model:
  - Both model a gene-level class is_a gene (GFF3Gene vs GeneAnnotation).
  - Both include dataset/context classes to describe files/sets (GFF3GeneSet vs GenomeAnnotation/AnnotationCollection).
  - Both capture file/dataset metadata: version, digest, content_url appear in their dataset/context classes.
  - Both carry organism/assembly context (species/assembly). gff3_gene uses species_taxon and genome build; genome_annotation uses GenomeAssembly (with thing with taxon mixin) and reference_assembly.
- Semantics overlap:
  - Biotype-like notion exists in both (gff3_gene.biotype with rich GeneBiotypeEnum vs genome_annotation.molecular_type with BioType).
  - Use of NCBIGene identifiers/prefixes anticipated in both.

Where they differ:
- Scope and granularity:
  - gff3_gene is GFF3 row-centric for gene features (Column 3 = gene), with precise coordinates and GFF3 semantics.
  - genome_annotation is higher-level, representing genes referenced from an annotation and linking to the annotation and assembly; it omits coordinates and most GFF3 specifics.
- Structure and classes:
  - gff3_gene classes: GFF3Gene (is_a gene), GFF3GeneSet (is_a dataset).
  - genome_annotation classes: GeneAnnotation (is_a gene), GenomeAnnotation (is_a genome), GenomeAssembly (is_a named thing; mixin: thing with taxon), AnnotationCollection (tree_root aggregator).
- Attributes/slots:
  - Present only in gff3_gene (GFF3 and harmonization specifics): seqid, source, feature_type (constrained to gene), start, end, score, strand, ensembl_gene_id, ncbi_gene_id (uriorcurie), locus_tag, gbkey, pseudo, pseudogene_subtype, note, genome_build, genome_build_accession, species_taxon; plus slot_usage mapping to GFF3 attributes (ID, Name, Alias, etc.).
  - Present only in genome_annotation (annotation wiring and authority): molecular_type, source_id, referenced_in→GenomeAnnotation, authority, reference_assembly→GenomeAssembly, strain; collection attributes annotations, genome_annotations, genome_assemblies.
- Enums and types:
  - gff3_gene: StrandEnum (+/-.? per GFF3), GeneFeatureType (fixed to gene, SO:0000704), GeneBiotypeEnum (richer set), custom one_based_int type.
  - genome_annotation: BioType (protein_coding, noncoding), AuthorityType (ENSEMBL, NCBI); no coordinate type.
- Prefix sets:
  - gff3_gene adds biolink, gff3, ENSEMBL, SO.
  - genome_annotation adds NCBIAssembly, NCBITaxon.
- Dataset/context modeling:
  - gff3_gene uses GFF3GeneSet (dataset) with records: GFF3Gene.
  - genome_annotation separates GenomeAnnotation (the dataset with authority/reference_assembly) from AnnotationCollection (a root that aggregates multiple GenomeAnnotation and GeneAnnotation instances).

Notes on potential alignment (optional):
- Map gff3_gene.biotype values to genome_annotation.BioType (many-to-one).
- Relate gff3_gene.species_taxon to GenomeAssembly/thing with taxon.
- Align GFF3GeneSet (version, digest, content_url) with GenomeAnnotation’s analogous metadata; authority could enrich gff3 provenance.
- Use GeneAnnotation.source_id to hold gff3 ID/ENSEMBL/NCBI accessions where appropriate.
