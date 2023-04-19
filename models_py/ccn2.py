from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union, Literal
from pydantic import BaseModel as BaseModel, Field
from linkml_runtime.linkml_model import Decimal

metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'
    
class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True, 
                validate_all = True, 
                underscore_attrs_are_private = True, 
                extra = 'forbid', 
                arbitrary_types_allowed = True):
    pass                    


class Rank(str, Enum):
    
    leaf_node = "leaf_node"
    family = "family"
    gross = "gross"
    
    

class Taxonomy(ConfiguredBaseModel):
    
    cell_set_accession: str = Field(None, description="""Primary identifier of the cell set. This field should be programmatically assigned, not edited.""")
    cell_type_name: Optional[str] = Field(None, description="""The primary name/symbol to be used for the (provisional) cell type defined by this cell set. This is left optional, but is strongly encouraged for every node that is linked.""")
    parent_cell_set_accession: str = Field(None, description="""The cell set accession of the parent cell set in the taxonomy. This field should be programmatically assigned, not edited.""")
    synonyms: Optional[str] = Field(None, description="""A list of alternative names for this cell type. Separate entries with a '|'. Do not use terms with a scope that is much narrower or broader than the cell type being described.""")
    synonym_provenance: Optional[str] = Field(None, description="""Each entry in the synonyms field should have a corresponding entry here, either the DOI of a supporting publication (in the form the form doi:10.1126/journal.abj6641) or the editor's ORCID (in the form: ORCID:01243-234-678). Multiple entries should be separated by a '|'.""")
    description: Optional[str] = Field(None, description="""Optional free text description of the cluster. This could be particularly useful for describing the properties of cells clustered from techniques that provide data on morphology, function and connectivity, e.g. patch-seq & epi-retro-seq.""")
    classifying_ontology_term_id: Optional[str] = Field(None, description="""The ID of an ontology term that classifies the cell type defined by this node.""")
    classifying_ontology_term_name: str = Field(None, description="""The name of the ontology term in the classification_id column""")
    classification_provenance: str = Field(None, description="""Either the DOI(s) of a supporting publication (in the form the form doi:10.1126/journal.abj6641) or the editor's ORCID (in the form: ORCID:01243-234-678). Multiple entries should be separated by a '|'.""")
    classification_comment: Optional[str] = Field(None, description="""A free text comment describing the evidence for this classification.""")
    rank: Optional[Rank] = Field(None, description="""Algorithmically generated hierarchical taxonomies can be complex, with many nodes between root and leaf and branches of variable depth. To simplify this for display and discussion it can be useful to assign nodes to a 3 level hierarchy, with leaf nodes at the bottom.""")
    


class CrossTaxonomyMapping(ConfiguredBaseModel):
    
    cell_set_accession: str = Field(None, description="""Primary identifier for cell set.""")
    cell_type_name: str = Field(None, description="""The primary name/symbol to be used for the cell type defined by this cell set.""")
    mapped_cell_set_accession: str = Field(None, description="""The accession (ID) of a cell set in a second taxonomy that this cell set maps to.""")
    mapped_cell_type_name: str = Field(None, description="""The name of the cell type corresponding to the mapped_cell_set_accession.""")
    evidence_comment: str = Field(None, description="""A free text description of the evidence supporting this mapping. If a similarity_score is include, please also include details of how this was calculated.""")
    similarity_score: Optional[float] = Field(None, description="""A score recording the similarity between mapped nodes.""", ge=0, le=1)
    provenance: Optional[str] = Field(None, description="""ORCID of the person doing the mapping using the syntax ORCID:0123-4567-890. Optionally include supporting publications using DOIs of the form doi:10.1126/journal.abj6641.""")
    


class LocationMapping(ConfiguredBaseModel):
    
    cell_set_accession: str = Field(None, description="""Primary identifier for cell set.""")
    cell_type_name: str = Field(None, description="""The primary name/symbol to be used for the cell type defined by this cell set.""")
    location_ontology_term_id: str = Field(None, description="""The ID of an ontology term that refers to a brain region that this cell type is located in. Ideally this should be the ID of a term defined as a region in a standard atlas.""")
    location_ontology_term_name: str = Field(None, description="""Name of the term whose ID is recorded in the ontology_term_id field.""")
    evidence_comment: Optional[str] = Field(None, description="""A comment describing the evidence for this location mapping""")
    supporting_data: Optional[str] = Field(None, description="""A link to data supporting this location mapping.""")
    provenance: str = Field(None, description="""ORCID of the person doing the mapping using the syntax ORCID:0123-4567-890. Optionally include supporting publications using DOIs of the form doi:10.1126/journal.abj6641.""")
    


class CellSetAccessionToCellMapping(ConfiguredBaseModel):
    
    sample: str = Field(None, description="""Cell sample identifier.""")
    cell_accessions: List[str] = Field(None, description="""List of cell set accession identifiers.""")
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
Taxonomy.update_forward_refs()
CrossTaxonomyMapping.update_forward_refs()
LocationMapping.update_forward_refs()
CellSetAccessionToCellMapping.update_forward_refs()

