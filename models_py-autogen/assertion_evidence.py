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


linkml_meta = LinkMLMeta({'default_prefix': 'brainkb',
     'default_range': 'string',
     'id': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
     'imports': ['linkml:types'],
     'name': 'assertion-evidence-schema',
     'prefixes': {'bican': {'prefix_prefix': 'bican',
                            'prefix_reference': 'https://identifiers.org/brain-bican/vocab/'},
                  'brainkb': {'prefix_prefix': 'brainkb',
                              'prefix_reference': 'https://brainkb.org/'},
                  'eco': {'prefix_prefix': 'eco',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/ECO_'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'sepio': {'prefix_prefix': 'sepio',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/SEPIO_'},
                  'spdx': {'prefix_prefix': 'spdx',
                           'prefix_reference': 'http://spdx.org/rdf/terms#'}},
     'source_file': 'assertion_evidence.yaml',
     'title': 'Assertion Evidence Schema'} )

class AssertionType(str, Enum):
    Positive = "Positive"
    Negative = "Negative"
    Inconclusive = "Inconclusive"


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


class SignificanceLevel(str, Enum):
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


class Significance(str, Enum):
    Clinical = "Clinical"
    NonClinical = "NonClinical"



class Assertion(ConfiguredBaseModel):
    """
    A statement made by a particular agent on a particular occasion that a particular proposition is true, based on the evaluation of one or more lines of evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sepio:Assertion',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
         'slot_usage': {'has_assertion_method': {'description': 'The '
                                                                'brainkb:hasAssertionMethod '
                                                                'property relates an '
                                                                'eco:Assertion to an '
                                                                'brainkb:AssertionMethod '
                                                                'that differentiates '
                                                                'different types of '
                                                                'assertions techniques '
                                                                'used while making an '
                                                                'assertion.',
                                                 'name': 'has_assertion_method'},
                        'has_data_annotation': {'name': 'has_data_annotation',
                                                'range': 'DataAnnotation'},
                        'is_associated_with': {'description': 'The '
                                                              'brainkb:isAssociatedWith '
                                                              'property establishes '
                                                              'relationships between '
                                                              'different entities:it '
                                                              'links sepio:Assertion '
                                                              'to '
                                                              'brainkb:AssertionSummary, '
                                                              'indicating the '
                                                              'association between an '
                                                              'assertion and its '
                                                              'corresponding summary.',
                                               'name': 'is_associated_with',
                                               'range': 'AssertionSummary'}}})

    has_assertion_method: Optional[AssertionMethod] = Field(None, description="""The brainkb:hasAssertionMethod property relates an eco:Assertion to an brainkb:AssertionMethod that differentiates different types of assertions techniques used while making an assertion.""", json_schema_extra = { "linkml_meta": {'alias': 'hasAssertionMethod',
         'domain_of': ['Assertion'],
         'slot_uri': 'brainkb:hasAssertionMethod'} })
    is_associated_with: Optional[AssertionSummary] = Field(None, description="""The brainkb:isAssociatedWith property establishes relationships between different entities:it links sepio:Assertion to brainkb:AssertionSummary, indicating the association between an assertion and its corresponding summary.""", json_schema_extra = { "linkml_meta": {'alias': 'is_associated_with', 'domain_of': ['Assertion', 'Agent', 'Evidence']} })
    has_data_annotation: Optional[DataAnnotation] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'has_data_annotation', 'domain_of': ['Assertion']} })
    has_assertion_category: Optional[Categories] = Field(None, description="""The brainkb:hasAssertionCategory property relates brainkb:Evidence and brainkb:Categories, specifying the classification or category that the assertion belongs to.""", json_schema_extra = { "linkml_meta": {'alias': 'hasAssertionCategory',
         'domain_of': ['Assertion'],
         'slot_uri': 'brainkb:hasAssertionCategory'} })
    has_assertion_text: Optional[str] = Field(None, description="""The brainkb:hasAssertionText property relates an eco:Assertion to an xsd:string, providing a textual excerpt of the assertion being made.""", json_schema_extra = { "linkml_meta": {'alias': 'hasAssertionText',
         'domain_of': ['Assertion'],
         'slot_uri': 'brainkb:hasAssertionText'} })


class Document(ConfiguredBaseModel):
    """
    A collection of information content entities intended to be understood together as a whole
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sepio:Document',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    pass


class Activity(ConfiguredBaseModel):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    ended_at_time: Optional[datetime ] = Field(None, description="""The prov:endedAtTime establishes the relationship between prov:Activity and xsd:DateTime that allows one to specify the time when the activity ended.""", json_schema_extra = { "linkml_meta": {'alias': 'endedAtTime', 'domain_of': ['Activity']} })
    started_at_time: Optional[datetime ] = Field(None, description="""The prov:startedAtTime establishes the relationship between prov:Activity and xsd:DateTime that allows one to specify the time when the activity started.""", json_schema_extra = { "linkml_meta": {'alias': 'startedAtTime', 'domain_of': ['Activity']} })


class Agent(ConfiguredBaseModel):
    """
    An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Agent',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
         'slot_usage': {'is_associated_with': {'description': 'The '
                                                              'brainkb:isAssociatedWith '
                                                              'property establishes '
                                                              'relationships between '
                                                              'different entities: it '
                                                              'connects prov:Agent to '
                                                              'prov:Activity, '
                                                              'reflecting the '
                                                              'involvement or '
                                                              'connection between an '
                                                              'agent and an activity.',
                                               'name': 'is_associated_with',
                                               'range': 'Activity'}}})

    is_associated_with: Optional[Activity] = Field(None, description="""The brainkb:isAssociatedWith property establishes relationships between different entities: it connects prov:Agent to prov:Activity, reflecting the involvement or connection between an agent and an activity.""", json_schema_extra = { "linkml_meta": {'alias': 'is_associated_with', 'domain_of': ['Assertion', 'Agent', 'Evidence']} })


class AssertionSummary(ConfiguredBaseModel):
    """
    A summary is a brief statement or description of the main points, especially as a conclusion to a work about the assertion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'brainkb:AssertionSummary',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    has_assertion_summary: Optional[str] = Field(None, description="""The brainkb:hasAssertionSummary property relates a brainkb:AssertionSummary to an xsd:string, providing a concise overview that differentiates various assertions. This summary encapsulates the core content of the assertion, allowing for easy identification and understanding of its essence.""", json_schema_extra = { "linkml_meta": {'alias': 'hasAssertionSummary',
         'domain_of': ['AssertionSummary'],
         'slot_uri': 'brainkb:hasAssertionSummary'} })


class EvidenceSummary(ConfiguredBaseModel):
    """
    A summary is a brief statement or description of the main points, especially as a conclusion to a work about the evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'brainkb:EvidenceSummary',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    has_evidence_summary: Optional[str] = Field(None, description="""The brainkb:hasEvidenceSummary property relates a brainkb:EvidenceSummary to an xsd:string, providing a concise overview that differentiates various evidence. This summary encapsulates the core content of the evidence, allowing for easy identification and understanding of its essence.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvidenceSummary',
         'domain_of': ['EvidenceSummary'],
         'slot_uri': 'brainkb:hasEvidenceSummary'} })


class AssertionMethod(ConfiguredBaseModel):
    """
    A means by which a statement is made about the entity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'eco:0000217',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    pass


class DataAnnotation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'brainkb:DataAnnotation',
         'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema'})

    pass


class Evidence(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://identifiers.org/brain-bican/assertion-evidence-schema',
         'slot_usage': {'is_associated_with': {'description': 'The '
                                                              'brainkb:isAssociatedWith '
                                                              'property establishes '
                                                              'relationships between '
                                                              'different entities: it '
                                                              'associates eco:Evidence '
                                                              'with '
                                                              'brainkb:EvidenceSummary, '
                                                              'signifying the '
                                                              'connection between '
                                                              'evidence and its '
                                                              'summarized '
                                                              'representation.',
                                               'name': 'is_associated_with',
                                               'range': 'EvidenceSummary'},
                        'used_in': {'name': 'used_in'}}})

    used_in: Optional[Assertion] = Field(None, description="""The eco:used_in property establishes a relationship between eco:Evidence and eco:Assertion, indicating that the evidence is utilized to support the corresponding assertion.""", json_schema_extra = { "linkml_meta": {'alias': 'used_in', 'domain_of': ['Evidence']} })
    is_associated_with: Optional[EvidenceSummary] = Field(None, description="""The brainkb:isAssociatedWith property establishes relationships between different entities: it associates eco:Evidence with brainkb:EvidenceSummary, signifying the connection between evidence and its summarized representation.""", json_schema_extra = { "linkml_meta": {'alias': 'is_associated_with', 'domain_of': ['Assertion', 'Agent', 'Evidence']} })
    has_evidence_category: Optional[Categories] = Field(None, description="""The brainkb:hasEvidenceCategory property relates brainkb:Evidence and brainkb:Categories, specifying the classification or category that the evidence belongs to.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvidenceCategory',
         'domain_of': ['Evidence'],
         'slot_uri': 'brainkb:hasEvidenceCategory'} })
    has_evidence_text: Optional[str] = Field(None, description="""The brainkb:hasEvidenceText property relates an eco:Evidence to an xsd:string, providing a textual excerpt of the evidence supporting the assertion.""", json_schema_extra = { "linkml_meta": {'alias': 'hasEvidenceText',
         'domain_of': ['Evidence'],
         'slot_uri': 'brainkb:hasEvidenceText'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Assertion.model_rebuild()
Document.model_rebuild()
Activity.model_rebuild()
Agent.model_rebuild()
AssertionSummary.model_rebuild()
EvidenceSummary.model_rebuild()
AssertionMethod.model_rebuild()
DataAnnotation.model_rebuild()
Evidence.model_rebuild()

