from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    ClassVar,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        RootModel,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'ccn2',
     'default_range': 'string',
     'id': 'CCN2',
     'imports': ['linkml:types'],
     'name': 'CCN2',
     'prefixes': {'ccn2': {'prefix_prefix': 'ccn2',
                           'prefix_reference': 'https://github.com/brain-bican/CCN2'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'ccn2.yaml'} )

class Rank(str, Enum):
    leaf_node = "leaf_node"
    family = "family"
    gross = "gross"



class Taxonomy(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'CCN2',
         'slot_usage': {'cell set accession': {'description': 'Primary identifier of '
                                                              'the cell set. This '
                                                              'field should be '
                                                              'programmatically '
                                                              'assigned, not edited.',
                                               'name': 'cell set accession',
                                               'readonly': 'True',
                                               'required': True},
                        'cell type name': {'description': 'The primary name/symbol to '
                                                          'be used for the '
                                                          '(provisional) cell type '
                                                          'defined by this cell set. '
                                                          'This is left optional, but '
                                                          'is strongly encouraged for '
                                                          'every node that is linked.',
                                           'name': 'cell type name'},
                        'classification provenance': {'name': 'classification '
                                                              'provenance',
                                                      'required': True},
                        'classifying ontology term name': {'name': 'classifying '
                                                                   'ontology term name',
                                                           'required': True},
                        'parent cell set accession': {'name': 'parent cell set '
                                                              'accession',
                                                      'required': True}}})

    cell_set_accession: str = Field(..., description="""Primary identifier of the cell set. This field should be programmatically assigned, not edited.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_set_accession',
         'domain_of': ['taxonomy', 'cross taxonomy mapping', 'location mapping'],
         'readonly': 'True'} })
    cell_type_name: Optional[str] = Field(None, description="""The primary name/symbol to be used for the (provisional) cell type defined by this cell set. This is left optional, but is strongly encouraged for every node that is linked.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_type_name',
         'domain_of': ['taxonomy', 'cross taxonomy mapping', 'location mapping']} })
    parent_cell_set_accession: str = Field(..., description="""The cell set accession of the parent cell set in the taxonomy. This field should be programmatically assigned, not edited.""", json_schema_extra = { "linkml_meta": {'alias': 'parent_cell_set_accession', 'domain_of': ['taxonomy']} })
    synonyms: Optional[str] = Field(None, description="""A list of alternative names for this cell type. Separate entries with a '|'. Do not use terms with a scope that is much narrower or broader than the cell type being described.""", json_schema_extra = { "linkml_meta": {'alias': 'synonyms', 'domain_of': ['taxonomy']} })
    synonym_provenance: Optional[str] = Field(None, description="""Each entry in the synonyms field should have a corresponding entry here, either the DOI of a supporting publication (in the form the form doi:10.1126/journal.abj6641) or the editor's ORCID (in the form: ORCID:01243-234-678). Multiple entries should be separated by a '|'.""", json_schema_extra = { "linkml_meta": {'alias': 'synonym_provenance', 'domain_of': ['taxonomy']} })
    description: Optional[str] = Field(None, description="""Optional free text description of the cluster. This could be particularly useful for describing the properties of cells clustered from techniques that provide data on morphology, function and connectivity, e.g. patch-seq & epi-retro-seq.""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['taxonomy']} })
    classifying_ontology_term_id: Optional[str] = Field(None, description="""The ID of an ontology term that classifies the cell type defined by this node.""", json_schema_extra = { "linkml_meta": {'alias': 'classifying_ontology_term_id', 'domain_of': ['taxonomy']} })
    classifying_ontology_term_name: str = Field(..., description="""The name of the ontology term in the classification_id column""", json_schema_extra = { "linkml_meta": {'alias': 'classifying_ontology_term_name', 'domain_of': ['taxonomy']} })
    classification_provenance: str = Field(..., description="""Either the DOI(s) of a supporting publication (in the form the form doi:10.1126/journal.abj6641) or the editor's ORCID (in the form: ORCID:01243-234-678). Multiple entries should be separated by a '|'.""", json_schema_extra = { "linkml_meta": {'alias': 'classification_provenance', 'domain_of': ['taxonomy']} })
    classification_comment: Optional[str] = Field(None, description="""A free text comment describing the evidence for this classification.""", json_schema_extra = { "linkml_meta": {'alias': 'classification_comment', 'domain_of': ['taxonomy']} })
    rank: Optional[Rank] = Field(None, description="""Algorithmically generated hierarchical taxonomies can be complex, with many nodes between root and leaf and branches of variable depth. To simplify this for display and discussion it can be useful to assign nodes to a 3 level hierarchy, with leaf nodes at the bottom.""", json_schema_extra = { "linkml_meta": {'alias': 'rank', 'domain_of': ['taxonomy']} })


class CrossTaxonomyMapping(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'CCN2',
         'slot_usage': {'cell set accession': {'name': 'cell set accession',
                                               'required': True},
                        'cell type name': {'name': 'cell type name', 'required': True},
                        'evidence comment': {'description': 'A free text description '
                                                            'of the evidence '
                                                            'supporting this mapping. '
                                                            'If a similarity_score is '
                                                            'include, please also '
                                                            'include details of how '
                                                            'this was calculated.',
                                             'name': 'evidence comment',
                                             'required': True},
                        'mapped cell set accession': {'name': 'mapped cell set '
                                                              'accession',
                                                      'required': True},
                        'mapped cell type name': {'name': 'mapped cell type name',
                                                  'required': True}}})

    cell_set_accession: str = Field(..., description="""Primary identifier for cell set.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_set_accession',
         'domain_of': ['taxonomy', 'cross taxonomy mapping', 'location mapping']} })
    cell_type_name: str = Field(..., description="""The primary name/symbol to be used for the cell type defined by this cell set.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_type_name',
         'domain_of': ['taxonomy', 'cross taxonomy mapping', 'location mapping']} })
    mapped_cell_set_accession: str = Field(..., description="""The accession (ID) of a cell set in a second taxonomy that this cell set maps to.""", json_schema_extra = { "linkml_meta": {'alias': 'mapped_cell_set_accession', 'domain_of': ['cross taxonomy mapping']} })
    mapped_cell_type_name: str = Field(..., description="""The name of the cell type corresponding to the mapped_cell_set_accession.""", json_schema_extra = { "linkml_meta": {'alias': 'mapped_cell_type_name', 'domain_of': ['cross taxonomy mapping']} })
    evidence_comment: str = Field(..., description="""A free text description of the evidence supporting this mapping. If a similarity_score is include, please also include details of how this was calculated.""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_comment',
         'domain_of': ['cross taxonomy mapping', 'location mapping']} })
    similarity_score: Optional[float] = Field(None, description="""A score recording the similarity between mapped nodes.""", ge=0, le=1, json_schema_extra = { "linkml_meta": {'alias': 'similarity_score', 'domain_of': ['cross taxonomy mapping']} })
    provenance: Optional[str] = Field(None, description="""ORCID of the person doing the mapping using the syntax ORCID:0123-4567-890. Optionally include supporting publications using DOIs of the form doi:10.1126/journal.abj6641.""", json_schema_extra = { "linkml_meta": {'alias': 'provenance',
         'domain_of': ['cross taxonomy mapping', 'location mapping']} })


class LocationMapping(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'CCN2',
         'slot_usage': {'cell set accession': {'name': 'cell set accession',
                                               'required': True},
                        'cell type name': {'name': 'cell type name', 'required': True},
                        'evidence comment': {'description': 'A comment describing the '
                                                            'evidence for this '
                                                            'location mapping',
                                             'name': 'evidence comment'},
                        'location ontology term id': {'name': 'location ontology term '
                                                              'id',
                                                      'required': True},
                        'location ontology term name': {'name': 'location ontology '
                                                                'term name',
                                                        'required': True},
                        'provenance': {'name': 'provenance', 'required': True}}})

    cell_set_accession: str = Field(..., description="""Primary identifier for cell set.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_set_accession',
         'domain_of': ['taxonomy', 'cross taxonomy mapping', 'location mapping']} })
    cell_type_name: str = Field(..., description="""The primary name/symbol to be used for the cell type defined by this cell set.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_type_name',
         'domain_of': ['taxonomy', 'cross taxonomy mapping', 'location mapping']} })
    location_ontology_term_id: str = Field(..., description="""The ID of an ontology term that refers to a brain region that this cell type is located in. Ideally this should be the ID of a term defined as a region in a standard atlas.""", json_schema_extra = { "linkml_meta": {'alias': 'location_ontology_term_id', 'domain_of': ['location mapping']} })
    location_ontology_term_name: str = Field(..., description="""Name of the term whose ID is recorded in the ontology_term_id field.""", json_schema_extra = { "linkml_meta": {'alias': 'location_ontology_term_name', 'domain_of': ['location mapping']} })
    evidence_comment: Optional[str] = Field(None, description="""A comment describing the evidence for this location mapping""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_comment',
         'domain_of': ['cross taxonomy mapping', 'location mapping']} })
    supporting_data: Optional[str] = Field(None, description="""A link to data supporting this location mapping.""", json_schema_extra = { "linkml_meta": {'alias': 'supporting_data', 'domain_of': ['location mapping']} })
    provenance: str = Field(..., description="""ORCID of the person doing the mapping using the syntax ORCID:0123-4567-890. Optionally include supporting publications using DOIs of the form doi:10.1126/journal.abj6641.""", json_schema_extra = { "linkml_meta": {'alias': 'provenance',
         'domain_of': ['cross taxonomy mapping', 'location mapping']} })


class CellSetAccessionToCellMapping(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'CCN2',
         'slot_usage': {'cell accessions': {'name': 'cell accessions',
                                            'required': True},
                        'sample': {'name': 'sample', 'required': True}}})

    sample: str = Field(..., description="""Cell sample identifier.""", json_schema_extra = { "linkml_meta": {'alias': 'sample', 'domain_of': ['cell set accession to cell mapping']} })
    cell_accessions: List[str] = Field(..., description="""List of cell set accession identifiers.""", json_schema_extra = { "linkml_meta": {'alias': 'cell_accessions',
         'domain_of': ['cell set accession to cell mapping']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Taxonomy.model_rebuild()
CrossTaxonomyMapping.model_rebuild()
LocationMapping.model_rebuild()
CellSetAccessionToCellMapping.model_rebuild()

