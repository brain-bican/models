# Auto generated from ccn.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-12T16:12:47
# Schema: CCN2
#
# id: CCN2
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CCN2 = CurieNamespace('ccn2', 'https://github.com/brain-bican/CCN2')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CCN2


# Types

# Class references



@dataclass
class Taxonomy(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCN2.Taxonomy
    class_class_curie: ClassVar[str] = "ccn2:Taxonomy"
    class_name: ClassVar[str] = "taxonomy"
    class_model_uri: ClassVar[URIRef] = CCN2.Taxonomy

    cell_set_accession: str = None
    parent_cell_set_accession: str = None
    classifying_ontology_term_name: str = None
    classification_provenance: str = None
    cell_type_name: Optional[str] = None
    synonyms: Optional[str] = None
    synonym_provenance: Optional[str] = None
    description: Optional[str] = None
    classifying_ontology_term_id: Optional[str] = None
    classification_comment: Optional[str] = None
    rank: Optional[Union[str, "Rank"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell_set_accession):
            self.MissingRequiredField("cell_set_accession")
        if not isinstance(self.cell_set_accession, str):
            self.cell_set_accession = str(self.cell_set_accession)

        if self._is_empty(self.parent_cell_set_accession):
            self.MissingRequiredField("parent_cell_set_accession")
        if not isinstance(self.parent_cell_set_accession, str):
            self.parent_cell_set_accession = str(self.parent_cell_set_accession)

        if self._is_empty(self.classifying_ontology_term_name):
            self.MissingRequiredField("classifying_ontology_term_name")
        if not isinstance(self.classifying_ontology_term_name, str):
            self.classifying_ontology_term_name = str(self.classifying_ontology_term_name)

        if self._is_empty(self.classification_provenance):
            self.MissingRequiredField("classification_provenance")
        if not isinstance(self.classification_provenance, str):
            self.classification_provenance = str(self.classification_provenance)

        if self.cell_type_name is not None and not isinstance(self.cell_type_name, str):
            self.cell_type_name = str(self.cell_type_name)

        if self.synonyms is not None and not isinstance(self.synonyms, str):
            self.synonyms = str(self.synonyms)

        if self.synonym_provenance is not None and not isinstance(self.synonym_provenance, str):
            self.synonym_provenance = str(self.synonym_provenance)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.classifying_ontology_term_id is not None and not isinstance(self.classifying_ontology_term_id, str):
            self.classifying_ontology_term_id = str(self.classifying_ontology_term_id)

        if self.classification_comment is not None and not isinstance(self.classification_comment, str):
            self.classification_comment = str(self.classification_comment)

        if self.rank is not None and not isinstance(self.rank, Rank):
            self.rank = Rank(self.rank)

        super().__post_init__(**kwargs)


@dataclass
class CrossTaxonomyMapping(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCN2.CrossTaxonomyMapping
    class_class_curie: ClassVar[str] = "ccn2:CrossTaxonomyMapping"
    class_name: ClassVar[str] = "cross taxonomy mapping"
    class_model_uri: ClassVar[URIRef] = CCN2.CrossTaxonomyMapping

    cell_set_accession: str = None
    cell_type_name: str = None
    mapped_cell_set_accession: str = None
    mapped_cell_type_name: str = None
    evidence_comment: str = None
    similarity_score: Optional[float] = None
    provenance: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell_set_accession):
            self.MissingRequiredField("cell_set_accession")
        if not isinstance(self.cell_set_accession, str):
            self.cell_set_accession = str(self.cell_set_accession)

        if self._is_empty(self.cell_type_name):
            self.MissingRequiredField("cell_type_name")
        if not isinstance(self.cell_type_name, str):
            self.cell_type_name = str(self.cell_type_name)

        if self._is_empty(self.mapped_cell_set_accession):
            self.MissingRequiredField("mapped_cell_set_accession")
        if not isinstance(self.mapped_cell_set_accession, str):
            self.mapped_cell_set_accession = str(self.mapped_cell_set_accession)

        if self._is_empty(self.mapped_cell_type_name):
            self.MissingRequiredField("mapped_cell_type_name")
        if not isinstance(self.mapped_cell_type_name, str):
            self.mapped_cell_type_name = str(self.mapped_cell_type_name)

        if self._is_empty(self.evidence_comment):
            self.MissingRequiredField("evidence_comment")
        if not isinstance(self.evidence_comment, str):
            self.evidence_comment = str(self.evidence_comment)

        if self.similarity_score is not None and not isinstance(self.similarity_score, float):
            self.similarity_score = float(self.similarity_score)

        if self.provenance is not None and not isinstance(self.provenance, str):
            self.provenance = str(self.provenance)

        super().__post_init__(**kwargs)


@dataclass
class LocationMapping(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCN2.LocationMapping
    class_class_curie: ClassVar[str] = "ccn2:LocationMapping"
    class_name: ClassVar[str] = "location mapping"
    class_model_uri: ClassVar[URIRef] = CCN2.LocationMapping

    cell_set_accession: str = None
    cell_type_name: str = None
    location_ontology_term_id: str = None
    location_ontology_term_name: str = None
    provenance: str = None
    evidence_comment: Optional[str] = None
    supporting_data: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell_set_accession):
            self.MissingRequiredField("cell_set_accession")
        if not isinstance(self.cell_set_accession, str):
            self.cell_set_accession = str(self.cell_set_accession)

        if self._is_empty(self.cell_type_name):
            self.MissingRequiredField("cell_type_name")
        if not isinstance(self.cell_type_name, str):
            self.cell_type_name = str(self.cell_type_name)

        if self._is_empty(self.location_ontology_term_id):
            self.MissingRequiredField("location_ontology_term_id")
        if not isinstance(self.location_ontology_term_id, str):
            self.location_ontology_term_id = str(self.location_ontology_term_id)

        if self._is_empty(self.location_ontology_term_name):
            self.MissingRequiredField("location_ontology_term_name")
        if not isinstance(self.location_ontology_term_name, str):
            self.location_ontology_term_name = str(self.location_ontology_term_name)

        if self._is_empty(self.provenance):
            self.MissingRequiredField("provenance")
        if not isinstance(self.provenance, str):
            self.provenance = str(self.provenance)

        if self.evidence_comment is not None and not isinstance(self.evidence_comment, str):
            self.evidence_comment = str(self.evidence_comment)

        if self.supporting_data is not None and not isinstance(self.supporting_data, str):
            self.supporting_data = str(self.supporting_data)

        super().__post_init__(**kwargs)


@dataclass
class CellSetAccessionToCellMapping(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CCN2.CellSetAccessionToCellMapping
    class_class_curie: ClassVar[str] = "ccn2:CellSetAccessionToCellMapping"
    class_name: ClassVar[str] = "cell set accession to cell mapping"
    class_model_uri: ClassVar[URIRef] = CCN2.CellSetAccessionToCellMapping

    sample: str = None
    cell_accessions: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sample):
            self.MissingRequiredField("sample")
        if not isinstance(self.sample, str):
            self.sample = str(self.sample)

        if self._is_empty(self.cell_accessions):
            self.MissingRequiredField("cell_accessions")
        if not isinstance(self.cell_accessions, list):
            self.cell_accessions = [self.cell_accessions] if self.cell_accessions is not None else []
        self.cell_accessions = [v if isinstance(v, str) else str(v) for v in self.cell_accessions]

        super().__post_init__(**kwargs)


# Enumerations
class Rank(EnumDefinitionImpl):

    leaf_node = PermissibleValue(text="leaf_node")
    family = PermissibleValue(text="family")
    gross = PermissibleValue(text="gross")

    _defn = EnumDefinition(
        name="Rank",
    )

# Slots
class slots:
    pass

slots.cell_set_accession = Slot(uri=CCN2.cell_set_accession, name="cell set accession", curie=CCN2.curie('cell_set_accession'),
                   model_uri=CCN2.cell_set_accession, domain=None, range=Optional[str])

slots.cell_type_name = Slot(uri=CCN2.cell_type_name, name="cell type name", curie=CCN2.curie('cell_type_name'),
                   model_uri=CCN2.cell_type_name, domain=None, range=Optional[str])

slots.parent_cell_set_accession = Slot(uri=CCN2.parent_cell_set_accession, name="parent cell set accession", curie=CCN2.curie('parent_cell_set_accession'),
                   model_uri=CCN2.parent_cell_set_accession, domain=None, range=Optional[str])

slots.synonyms = Slot(uri=CCN2.synonyms, name="synonyms", curie=CCN2.curie('synonyms'),
                   model_uri=CCN2.synonyms, domain=None, range=Optional[str])

slots.synonym_provenance = Slot(uri=CCN2.synonym_provenance, name="synonym provenance", curie=CCN2.curie('synonym_provenance'),
                   model_uri=CCN2.synonym_provenance, domain=None, range=Optional[str])

slots.description = Slot(uri=CCN2.description, name="description", curie=CCN2.curie('description'),
                   model_uri=CCN2.description, domain=None, range=Optional[str])

slots.classifying_ontology_term_id = Slot(uri=CCN2.classifying_ontology_term_id, name="classifying ontology term id", curie=CCN2.curie('classifying_ontology_term_id'),
                   model_uri=CCN2.classifying_ontology_term_id, domain=None, range=Optional[str])

slots.classifying_ontology_term_name = Slot(uri=CCN2.classifying_ontology_term_name, name="classifying ontology term name", curie=CCN2.curie('classifying_ontology_term_name'),
                   model_uri=CCN2.classifying_ontology_term_name, domain=None, range=Optional[str])

slots.classification_provenance = Slot(uri=CCN2.classification_provenance, name="classification provenance", curie=CCN2.curie('classification_provenance'),
                   model_uri=CCN2.classification_provenance, domain=None, range=Optional[str])

slots.classification_comment = Slot(uri=CCN2.classification_comment, name="classification comment", curie=CCN2.curie('classification_comment'),
                   model_uri=CCN2.classification_comment, domain=None, range=Optional[str])

slots.rank = Slot(uri=CCN2.rank, name="rank", curie=CCN2.curie('rank'),
                   model_uri=CCN2.rank, domain=None, range=Optional[Union[str, "Rank"]])

slots.mapped_cell_set_accession = Slot(uri=CCN2.mapped_cell_set_accession, name="mapped cell set accession", curie=CCN2.curie('mapped_cell_set_accession'),
                   model_uri=CCN2.mapped_cell_set_accession, domain=None, range=Optional[str])

slots.mapped_cell_type_name = Slot(uri=CCN2.mapped_cell_type_name, name="mapped cell type name", curie=CCN2.curie('mapped_cell_type_name'),
                   model_uri=CCN2.mapped_cell_type_name, domain=None, range=Optional[str])

slots.evidence_comment = Slot(uri=CCN2.evidence_comment, name="evidence comment", curie=CCN2.curie('evidence_comment'),
                   model_uri=CCN2.evidence_comment, domain=None, range=Optional[str])

slots.similarity_score = Slot(uri=CCN2.similarity_score, name="similarity score", curie=CCN2.curie('similarity_score'),
                   model_uri=CCN2.similarity_score, domain=None, range=Optional[float])

slots.provenance = Slot(uri=CCN2.provenance, name="provenance", curie=CCN2.curie('provenance'),
                   model_uri=CCN2.provenance, domain=None, range=Optional[str])

slots.location_ontology_term_id = Slot(uri=CCN2.location_ontology_term_id, name="location ontology term id", curie=CCN2.curie('location_ontology_term_id'),
                   model_uri=CCN2.location_ontology_term_id, domain=None, range=Optional[str])

slots.location_ontology_term_name = Slot(uri=CCN2.location_ontology_term_name, name="location ontology term name", curie=CCN2.curie('location_ontology_term_name'),
                   model_uri=CCN2.location_ontology_term_name, domain=None, range=Optional[str])

slots.supporting_data = Slot(uri=CCN2.supporting_data, name="supporting data", curie=CCN2.curie('supporting_data'),
                   model_uri=CCN2.supporting_data, domain=None, range=Optional[str])

slots.sample = Slot(uri=CCN2.sample, name="sample", curie=CCN2.curie('sample'),
                   model_uri=CCN2.sample, domain=None, range=Optional[str])

slots.cell_accessions = Slot(uri=CCN2.cell_accessions, name="cell accessions", curie=CCN2.curie('cell_accessions'),
                   model_uri=CCN2.cell_accessions, domain=None, range=Optional[Union[str, List[str]]])

slots.taxonomy_cell_set_accession = Slot(uri=CCN2.cell_set_accession, name="taxonomy_cell set accession", curie=CCN2.curie('cell_set_accession'),
                   model_uri=CCN2.taxonomy_cell_set_accession, domain=Taxonomy, range=str)

slots.taxonomy_cell_type_name = Slot(uri=CCN2.cell_type_name, name="taxonomy_cell type name", curie=CCN2.curie('cell_type_name'),
                   model_uri=CCN2.taxonomy_cell_type_name, domain=Taxonomy, range=Optional[str])

slots.taxonomy_parent_cell_set_accession = Slot(uri=CCN2.parent_cell_set_accession, name="taxonomy_parent cell set accession", curie=CCN2.curie('parent_cell_set_accession'),
                   model_uri=CCN2.taxonomy_parent_cell_set_accession, domain=Taxonomy, range=str)

slots.taxonomy_classifying_ontology_term_name = Slot(uri=CCN2.classifying_ontology_term_name, name="taxonomy_classifying ontology term name", curie=CCN2.curie('classifying_ontology_term_name'),
                   model_uri=CCN2.taxonomy_classifying_ontology_term_name, domain=Taxonomy, range=str)

slots.taxonomy_classification_provenance = Slot(uri=CCN2.classification_provenance, name="taxonomy_classification provenance", curie=CCN2.curie('classification_provenance'),
                   model_uri=CCN2.taxonomy_classification_provenance, domain=Taxonomy, range=str)

slots.cross_taxonomy_mapping_cell_set_accession = Slot(uri=CCN2.cell_set_accession, name="cross taxonomy mapping_cell set accession", curie=CCN2.curie('cell_set_accession'),
                   model_uri=CCN2.cross_taxonomy_mapping_cell_set_accession, domain=CrossTaxonomyMapping, range=str)

slots.cross_taxonomy_mapping_cell_type_name = Slot(uri=CCN2.cell_type_name, name="cross taxonomy mapping_cell type name", curie=CCN2.curie('cell_type_name'),
                   model_uri=CCN2.cross_taxonomy_mapping_cell_type_name, domain=CrossTaxonomyMapping, range=str)

slots.cross_taxonomy_mapping_mapped_cell_set_accession = Slot(uri=CCN2.mapped_cell_set_accession, name="cross taxonomy mapping_mapped cell set accession", curie=CCN2.curie('mapped_cell_set_accession'),
                   model_uri=CCN2.cross_taxonomy_mapping_mapped_cell_set_accession, domain=CrossTaxonomyMapping, range=str)

slots.cross_taxonomy_mapping_mapped_cell_type_name = Slot(uri=CCN2.mapped_cell_type_name, name="cross taxonomy mapping_mapped cell type name", curie=CCN2.curie('mapped_cell_type_name'),
                   model_uri=CCN2.cross_taxonomy_mapping_mapped_cell_type_name, domain=CrossTaxonomyMapping, range=str)

slots.cross_taxonomy_mapping_evidence_comment = Slot(uri=CCN2.evidence_comment, name="cross taxonomy mapping_evidence comment", curie=CCN2.curie('evidence_comment'),
                   model_uri=CCN2.cross_taxonomy_mapping_evidence_comment, domain=CrossTaxonomyMapping, range=str)

slots.location_mapping_cell_set_accession = Slot(uri=CCN2.cell_set_accession, name="location mapping_cell set accession", curie=CCN2.curie('cell_set_accession'),
                   model_uri=CCN2.location_mapping_cell_set_accession, domain=LocationMapping, range=str)

slots.location_mapping_cell_type_name = Slot(uri=CCN2.cell_type_name, name="location mapping_cell type name", curie=CCN2.curie('cell_type_name'),
                   model_uri=CCN2.location_mapping_cell_type_name, domain=LocationMapping, range=str)

slots.location_mapping_location_ontology_term_id = Slot(uri=CCN2.location_ontology_term_id, name="location mapping_location ontology term id", curie=CCN2.curie('location_ontology_term_id'),
                   model_uri=CCN2.location_mapping_location_ontology_term_id, domain=LocationMapping, range=str)

slots.location_mapping_location_ontology_term_name = Slot(uri=CCN2.location_ontology_term_name, name="location mapping_location ontology term name", curie=CCN2.curie('location_ontology_term_name'),
                   model_uri=CCN2.location_mapping_location_ontology_term_name, domain=LocationMapping, range=str)

slots.location_mapping_evidence_comment = Slot(uri=CCN2.evidence_comment, name="location mapping_evidence comment", curie=CCN2.curie('evidence_comment'),
                   model_uri=CCN2.location_mapping_evidence_comment, domain=LocationMapping, range=Optional[str])

slots.location_mapping_provenance = Slot(uri=CCN2.provenance, name="location mapping_provenance", curie=CCN2.curie('provenance'),
                   model_uri=CCN2.location_mapping_provenance, domain=LocationMapping, range=str)

slots.cell_set_accession_to_cell_mapping_sample = Slot(uri=CCN2.sample, name="cell set accession to cell mapping_sample", curie=CCN2.curie('sample'),
                   model_uri=CCN2.cell_set_accession_to_cell_mapping_sample, domain=CellSetAccessionToCellMapping, range=str)

slots.cell_set_accession_to_cell_mapping_cell_accessions = Slot(uri=CCN2.cell_accessions, name="cell set accession to cell mapping_cell accessions", curie=CCN2.curie('cell_accessions'),
                   model_uri=CCN2.cell_set_accession_to_cell_mapping_cell_accessions, domain=CellSetAccessionToCellMapping, range=Union[str, List[str]])
