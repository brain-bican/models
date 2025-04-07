# BICAN Knowledge Graph Models

## Background 
The BRAIN Initiative Cell Atlas Network (BICAN) is developing an extensible Brain Cell Knowledge Base (BCKB) to ingest and standardize comprehensive cell type information from BICAN's development of a multimodal, multi-species brain cell atlas and disseminate that atlas as an open and interactive community resource for advancing knowledge of the brain. As the first part of the BCKB project, BICAN will create an adaptive Knowledge Graph for linking brain cell information. A flexible graph-based data model will capture discrete and continuous cell type relationships. The data models listed below are used to ingest data into the Knowledge Graph.

## Data Models
### 1. Library Generation Model
The Library Generation Model is a data model designed to represent types and relationships of samples and digital data assets generated during processes that generate multimodal genomic data. The Library Generation Model can be used to formalize relationships between samples generated during processes in the Anatomical Level and Cellular Level conduced by the Specimen Portal and Sequence Library (SeqLib) Portal. The Specimen Portal focuses on tissue management from donors to brain slabs and annotated brain samples. The SeqLib Portal manages the workflow starting from tissue, all the way downstream to track data deposition to assay-dependent, data-modality-specific archives.<br>For further details, reference the [Neuroanatomy-anchored Information Management Platform](https://brain-specimenportal.org/).

### 2. Anatomical Structure Model
The Anatomical Structure Model is a data model designed to represent types and relationships of anatomical brain structures. The model can be used to formalize relationships between spatial definition, names, and metadata of these structures - and the parcellations they collectively comprise. 

### 3. Genome Annotation Model  
The Genome Annotation Model is a data model designed to represent types and relationships of an organism's annotated genome. The model can be used to formalize relationships between genes, genome assemblies, and organisms. 

### 4. Assertion Evidence Model 
The Assertion Evidence Model is a data model designed to represent the structure describing the relationship between a conclusion and the evidence that led to this conclusion. An assertion is the conclusion drawn from reasoning about Evidence. 

### 5. BKE Taxonomy Model
The BKE Taxonomy Model is a data model designed to represent the structure of the BKE Taxonomy. The BKE Taxonomy is a classifications of cell types and their hierarchical relationships in the mammalian brain.

## Using the Data Models 
Each data model listed above has a respective module in the Brain Knowledge Base Interaction Toolkit ([bkbit](https://pypi.org/project/bkbit/)). 