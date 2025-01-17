from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
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


linkml_meta = LinkMLMeta({'default_prefix': 'brainkb',
     'default_range': 'string',
     'id': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
     'imports': ['linkml:types'],
     'name': 'assertion-evidence-schema',
     'prefixes': {'bican': {'prefix_prefix': 'bican',
                            'prefix_reference': 'https://identifiers.org/brain-bican/vocab/'},
                  'braiankb': {'prefix_prefix': 'braiankb',
                               'prefix_reference': 'http://example.org/braiankb/'},
                  'brainkb': {'prefix_prefix': 'brainkb',
                              'prefix_reference': 'https://brainkb.org/'},
                  'datacite': {'prefix_prefix': 'datacite',
                               'prefix_reference': 'http://purl.org/spar/datacite/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'eco': {'prefix_prefix': 'eco',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/ECO_'},
                  'edam': {'prefix_prefix': 'edam',
                           'prefix_reference': 'http://edamontology.org/'},
                  'foaf': {'prefix_prefix': 'foaf',
                           'prefix_reference': 'http://xmlns.com/foaf/0.1/'},
                  'iao': {'prefix_prefix': 'iao',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/IAO_'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'oa': {'prefix_prefix': 'oa',
                         'prefix_reference': 'http://www.w3.org/ns/oa#'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'ro': {'prefix_prefix': 'ro',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/RO_'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'sepio': {'prefix_prefix': 'sepio',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/SEPIO_'},
                  'sio': {'prefix_prefix': 'sio',
                          'prefix_reference': 'http://semanticscience.org/resource/SIO_'},
                  'spdx': {'prefix_prefix': 'spdx',
                           'prefix_reference': 'http://spdx.org/rdf/terms#'}},
     'source_file': 'assertion_evidence.yaml',
     'title': 'Assertion Evidence Schema'} )

class Categories(str, Enum):
    Behavioral = "Behavioral"
    Biomarker = "Biomarker"
    DrugTarget = "DrugTarget"
    Genetic = "Genetic"
    ClinicalTrial = "ClinicalTrial"
    Etiologic = "Etiologic"
    Neuroimaging = "Neuroimaging"
    Electrophysiological = "Electrophysiological"
    Molecular = "Molecular"
    Pharmacological = "Pharmacological"
    Neuropsychological = "Neuropsychological"
    Neurogenetic = "Neurogenetic"
    Neurochemical = "Neurochemical"
    Neuroanatomical = "Neuroanatomical"
    Neurodevelopmental = "Neurodevelopmental"
    Neuroinflammatory = "Neuroinflammatory"
    Neuroplasticity = "Neuroplasticity"
    Neuropathological = "Neuropathological"
    Neurocomputational = "Neurocomputational"
    Neuroendocrine = "Neuroendocrine"
    Neuropharmacogenomic = "Neuropharmacogenomic"
    Neuroproteomic = "Neuroproteomic"
    Neurogenomic = "Neurogenomic"
    Epigenetic = "Epigenetic"
    Environmental = "Environmental"
    Translational = "Translational"
    Therapeutic = "Therapeutic"
    CognitiveNeuroscience = "CognitiveNeuroscience"


class EvidenceStrength(str, Enum):
    # P value less than 0.01
    HighlySignificant = "HighlySignificant"
    # P value less than 0.05
    Significant = "Significant"
    # P value less than 0.10
    MarginallySignificant = "MarginallySignificant"
    # P value greater than or equal to 0.10
    NotSignificant = "NotSignificant"
    # Specifies that the significance level is unknown as the information is not present in the study.
    Unknown = "Unknown"


class EvidenceDirection(str, Enum):
    supporting = "supporting"
    disputing = "disputing"
    inconclusive = "inconclusive"



class Activity(ConfiguredBaseModel):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
         'slot_usage': {'was_associate_with': {'name': 'was_associate_with',
                                               'range': 'Agent',
                                               'slot_uri': 'prov:wasAssociatedWith'}}})

    was_associate_with: Optional[Agent] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'was_associate_with',
         'domain_of': ['Activity'],
         'slot_uri': 'prov:wasAssociatedWith'} })
    endedAtTime: Optional[datetime ] = Field(default=None, description="""The prov:endedAtTime establishes the relationship between prov:Activity and xsd:DateTime that allows one to specify the time when the activity ended.""", json_schema_extra = { "linkml_meta": {'alias': 'endedAtTime', 'domain_of': ['Activity']} })
    startedAtTime: Optional[datetime ] = Field(default=None, description="""The prov:startedAtTime establishes the relationship between prov:Activity and xsd:DateTime that allows one to specify the time when the activity started.""", json_schema_extra = { "linkml_meta": {'alias': 'startedAtTime', 'domain_of': ['Activity']} })


class Agent(ConfiguredBaseModel):
    """
    An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Agent',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
         'slot_usage': {'has_identifier': {'name': 'has_identifier',
                                           'range': 'Identifier',
                                           'slot_uri': 'edam:has_identifier'}}})

    has_identifier: Optional[Identifier] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_identifier',
         'domain_of': ['Agent'],
         'slot_uri': 'edam:has_identifier'} })


class Annotation(ConfiguredBaseModel):
    """
    An annotation is a written explanatory or critical description, or other in-context information (e.g., pattern, motif, link), that has been associated with data or other types of information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'oa:Annotation',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    pass


class Assertion(ConfiguredBaseModel):
    """
    A statement made by a particular agent on a particular occasion that a particular proposition is true, based on the evaluation of one or more lines of evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sepio:0000001',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
         'slot_usage': {'has_annotation': {'name': 'has_annotation',
                                           'range': 'Annotation',
                                           'slot_uri': 'sio:000255'},
                        'has_evidence_line': {'description': 'A relationship between '
                                                             'an assertion or '
                                                             'proposition and an '
                                                             'evidence line used in '
                                                             'evaluating its validity.',
                                              'name': 'has_evidence_line',
                                              'range': 'EvidenceLine',
                                              'slot_uri': 'sepio:0000006'},
                        'was_generated_by': {'name': 'was_generated_by',
                                             'range': 'Activity',
                                             'slot_uri': 'prov:wasGeneratedBy'}}})

    has_annotation: Optional[Annotation] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_annotation',
         'domain_of': ['Assertion'],
         'slot_uri': 'sio:000255'} })
    was_generated_by: Optional[Activity] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Assertion', 'EvidenceLine'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    has_evidence_line: Optional[EvidenceLine] = Field(default=None, description="""A relationship between an assertion or proposition and an evidence line used in evaluating its validity.""", json_schema_extra = { "linkml_meta": {'alias': 'has_evidence_line',
         'domain_of': ['Assertion'],
         'slot_uri': 'sepio:0000006'} })
    has_assertion_category: Optional[Categories] = Field(default=None, description="""The brainkb:hasAssertionCategory property relates brainkb:Evidence and brainkb:Categories, specifying the classification or category that the assertion belongs to.""", json_schema_extra = { "linkml_meta": {'alias': 'has_assertion_category',
         'domain_of': ['Assertion'],
         'slot_uri': 'brainkb:has_assertion_category'} })
    has_assertion_description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_assertion_description',
         'domain_of': ['Assertion'],
         'slot_uri': 'brainkb:has_assertion_description'} })
    has_assertion_summary: Optional[str] = Field(default=None, description="""The brainkb:has_assertion_text property relates an eco:Assertion to an xsd:string, providing a textual excerpt of the assertion being made.""", json_schema_extra = { "linkml_meta": {'alias': 'has_assertion_summary',
         'domain_of': ['Assertion'],
         'slot_uri': 'brainkb:has_assertion_summary'} })


class CellAnnotation(Annotation):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'brainkb:CellAnnotation',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    pass


class EvidenceItem(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sepio:0000149',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
         'slot_usage': {'reference': {'name': 'reference',
                                      'range': 'Document',
                                      'slot_uri': 'sepio:0000442'}}})

    reference: Optional[Document] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'reference',
         'domain_of': ['EvidenceItem'],
         'slot_uri': 'sepio:0000442'} })


class Document(EvidenceItem):
    """
    A collection of information content entities intended to be understood together as a whole
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'iao:0000310',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    identifier: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'identifier',
         'domain_of': ['Document'],
         'slot_uri': 'datacite:identifier'} })
    reference: Optional[Document] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'reference',
         'domain_of': ['EvidenceItem'],
         'slot_uri': 'sepio:0000442'} })


class EvidenceLine(ConfiguredBaseModel):
    """
    An evidence line represents an independent and meaningful argument for or against a particular proposition, that is based on the interpretation of one or more pieces of information as evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sepio:0000002',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
         'slot_usage': {'has_evidence_item': {'description': 'A relation holding '
                                                             'between an evidence line '
                                                             'and an individual '
                                                             'information entity that '
                                                             'contributes to the '
                                                             'argument it represents.',
                                              'name': 'has_evidence_item',
                                              'range': 'EvidenceItem',
                                              'slot_uri': 'sepio:0000084'},
                        'was_generated_by': {'name': 'was_generated_by',
                                             'range': 'Activity',
                                             'slot_uri': 'prov:wasGeneratedBy'}}})

    has_evidence_item: Optional[EvidenceItem] = Field(default=None, description="""A relation holding between an evidence line and an individual information entity that contributes to the argument it represents.""", json_schema_extra = { "linkml_meta": {'alias': 'has_evidence_item',
         'domain_of': ['EvidenceLine'],
         'slot_uri': 'sepio:0000084'} })
    was_generated_by: Optional[Activity] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['Assertion', 'EvidenceLine'],
         'slot_uri': 'prov:wasGeneratedBy'} })
    evidence_direction: Optional[EvidenceDirection] = Field(default=None, description="""A relation indicating whether an evidence line supports or disputes a target proposition (or represents inconclusive evidence that is not sufficient for either).""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_direction',
         'domain_of': ['EvidenceLine'],
         'slot_uri': 'sepio:0000183'} })
    evidence_line_strength: Optional[EvidenceStrength] = Field(default=None, description="""A relation describing the degree of support provided by an evidence line for a target assertion or proposition.""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_line_strength',
         'domain_of': ['EvidenceLine'],
         'slot_uri': 'sepio:0000132'} })
    has_evidence_category: Optional[Categories] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_evidence_category',
         'domain_of': ['EvidenceLine'],
         'slot_uri': 'brainkb:has_evidence_category'} })
    has_evidenceline_description: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_evidenceline_description',
         'domain_of': ['EvidenceLine'],
         'slot_uri': 'braiankb:has_evidenceline_description'} })


class Group(Agent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'foaf:Group',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    has_identifier: Optional[Identifier] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_identifier',
         'domain_of': ['Agent'],
         'slot_uri': 'edam:has_identifier'} })


class Identifier(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'edam:data_0842',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    pass


class Organization(Group):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Organization',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    has_identifier: Optional[Identifier] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_identifier',
         'domain_of': ['Agent'],
         'slot_uri': 'edam:has_identifier'} })


class Person(Agent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Person',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
         'slot_usage': {'member': {'name': 'member',
                                   'range': 'Organization',
                                   'slot_uri': 'foaf:member'}}})

    member: Optional[Organization] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'member', 'domain_of': ['Person'], 'slot_uri': 'foaf:member'} })
    has_identifier: Optional[Identifier] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_identifier',
         'domain_of': ['Agent'],
         'slot_uri': 'edam:has_identifier'} })


class PersonIdentifier(Identifier):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'edam:data_2118',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    pass


class OrcidIdentifier(PersonIdentifier):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'edam:data_4022',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    pass


class SoftwareAgent(Agent):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:SoftwareAgent',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    has_identifier: Optional[Identifier] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'has_identifier',
         'domain_of': ['Agent'],
         'slot_uri': 'edam:has_identifier'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Activity.model_rebuild()
Agent.model_rebuild()
Annotation.model_rebuild()
Assertion.model_rebuild()
CellAnnotation.model_rebuild()
EvidenceItem.model_rebuild()
Document.model_rebuild()
EvidenceLine.model_rebuild()
Group.model_rebuild()
Identifier.model_rebuild()
Organization.model_rebuild()
Person.model_rebuild()
PersonIdentifier.model_rebuild()
OrcidIdentifier.model_rebuild()
SoftwareAgent.model_rebuild()

