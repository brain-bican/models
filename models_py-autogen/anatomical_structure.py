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


linkml_meta = LinkMLMeta({'default_prefix': 'AnS',
     'default_range': 'string',
     'description': 'The Anatomical Structure schema is designed to represent '
                    'types and relationships of anatomical brain structures. ',
     'id': 'https://w3id.org/my-org/anatomical-structure-schema',
     'imports': ['linkml:types', 'anatomical_structure_core'],
     'license': 'MIT',
     'name': 'anatomical-structure-schema',
     'prefixes': {'AnS': {'prefix_prefix': 'AnS',
                          'prefix_reference': 'https://w3id.org/my-org/anatomical-structure-schema/'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'settings': {'ColorHexTriplet': {'setting_key': 'ColorHexTriplet',
                                      'setting_value': '#[0-9a-fA-F]{6}'},
                  'PositiveFloat': {'setting_key': 'PositiveFloat',
                                    'setting_value': '^[+]?\\d*\\.?\\d+$'}},
     'source_file': 'anatomical_structure.yaml',
     'title': 'Anatomical Structure Schema'} )

class ANATOMICALDIRECTION(str, Enum):
    """
    A controlled vocabulary term defining axis direction in terms of anatomical direction.
    """
    left_to_right = "left_to_right"
    posterior_to_anterior = "posterior_to_anterior"
    inferior_to_superior = "inferior_to_superior"
    superior_to_inferior = "superior_to_inferior"
    anterior_to_posterior = "anterior_to_posterior"


class DISTANCEUNIT(str, Enum):
    millimeter = "mm"
    micrometer = "um"
    meter = "m"



class NamedThing(ConfiguredBaseModel):
    """
    Core base entity for Anatomical Structure schema representing an entity with an identifier  name and description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/my-org/anatomical-structure-core-schema'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/NamedThing","AnS:NamedThing"]] = Field(default=["AnS:NamedThing"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


class VersionedNamedThing(NamedThing):
    """
    Core base entity for Anatomical Structure schema representing an versioned named thing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/my-org/anatomical-structure-core-schema'})

    version: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['VersionedNamedThing']} })
    revision_of: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'revision_of', 'domain_of': ['VersionedNamedThing']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/VersionedNamedThing","AnS:VersionedNamedThing"]] = Field(default=["AnS:VersionedNamedThing"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


class ImageDataset(VersionedNamedThing):
    """
    An image dataset is versioned release of a multidimensional regular grid of measurements  and metadata required for a morphological representation of an entity such as an anatomical  structure (ref: OBI_0003327, RRID:SCR_006266)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema',
         'slot_usage': {'revision_of': {'any_of': [{'range': 'ImageDataset'},
                                                   {'range': 'string'}],
                                        'name': 'revision_of'}}})

    x_direction: Optional[ANATOMICALDIRECTION] = Field(default=None, description="""A controlled vocabulary attribute defining the x axis direction in terms of anatomical  direction.""", json_schema_extra = { "linkml_meta": {'alias': 'x_direction', 'domain_of': ['ImageDataset']} })
    y_direction: Optional[ANATOMICALDIRECTION] = Field(default=None, description="""A controlled vocabulary attribute defining the y axis direction in terms of anatomical  direction.""", json_schema_extra = { "linkml_meta": {'alias': 'y_direction', 'domain_of': ['ImageDataset']} })
    z_direction: Optional[ANATOMICALDIRECTION] = Field(default=None, description="""A controlled vocabulary attribute defining the z axis direction in terms of anatomical  direction.""", json_schema_extra = { "linkml_meta": {'alias': 'z_direction', 'domain_of': ['ImageDataset']} })
    x_size: Optional[int] = Field(default=None, description="""The number of pixels/voxels (size) along the x axis.""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'x_size', 'domain_of': ['ImageDataset']} })
    y_size: Optional[int] = Field(default=None, description="""The number of pixels/voxels (size) along the y axis.""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'y_size', 'domain_of': ['ImageDataset']} })
    z_size: Optional[int] = Field(default=None, description="""The number of pixels/voxels (size) along the y axis.""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'z_size', 'domain_of': ['ImageDataset']} })
    x_resolution: Optional[float] = Field(default=None, description="""The resolution (length / pixel) in along the x axis (numerical value part).""", json_schema_extra = { "linkml_meta": {'alias': 'x_resolution',
         'domain_of': ['ImageDataset'],
         'structured_pattern': {'syntax': '{PositiveFloat}'}} })
    y_resolution: Optional[float] = Field(default=None, description="""The resolution (length / pixel) in along the y axis (numerical value part).""", json_schema_extra = { "linkml_meta": {'alias': 'y_resolution',
         'domain_of': ['ImageDataset'],
         'structured_pattern': {'syntax': '{PositiveFloat}'}} })
    z_resolution: Optional[float] = Field(default=None, description="""The resolution (length / pixel) in along the z axis (numerical value part).""", json_schema_extra = { "linkml_meta": {'alias': 'z_resolution',
         'domain_of': ['ImageDataset'],
         'structured_pattern': {'syntax': '{PositiveFloat}'}} })
    unit: Optional[DISTANCEUNIT] = Field(default=None, description="""A controlled vocabulary attribute defining the length unit of the x, y, and z  resolution values.""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['ImageDataset']} })
    version: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['VersionedNamedThing']} })
    revision_of: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'revision_of',
         'any_of': [{'range': 'ImageDataset'}, {'range': 'string'}],
         'domain_of': ['VersionedNamedThing']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ImageDataset","AnS:ImageDataset"]] = Field(default=["AnS:ImageDataset"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


class AnatomicalSpace(VersionedNamedThing):
    """
    An anatomical space is versioned release of a mathematical space with a defined mapping  between the anatomical axes and the mathematical axes. An anatomical space may be defined by  a reference image chosen as the biological reference for an anatomical structure of interest  derived from a single or multiple specimens (ref: ILX:0777106, RRID:SCR_023499)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema',
         'slot_usage': {'revision_of': {'any_of': [{'range': 'AnatomicalSpace'},
                                                   {'range': 'string'}],
                                        'name': 'revision_of'}}})

    measures: str = Field(default=..., description="""Reference to the specific image dataset used to define the anatomical space.""", json_schema_extra = { "linkml_meta": {'alias': 'measures',
         'any_of': [{'range': 'ImageDataset'}, {'range': 'string'}],
         'domain_of': ['AnatomicalSpace']} })
    version: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['VersionedNamedThing']} })
    revision_of: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'revision_of',
         'any_of': [{'range': 'AnatomicalSpace'}, {'range': 'string'}],
         'domain_of': ['VersionedNamedThing']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/AnatomicalSpace","AnS:AnatomicalSpace"]] = Field(default=["AnS:AnatomicalSpace"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


class ParcellationTerminology(VersionedNamedThing):
    """
    A parcellation terminology is a versioned release set of terms that can be used to label  annotations in an atlas, providing human readability and context and allowing communication  about brain locations and structural properties. Typically, a terminology is a set of  descriptive anatomical terms following a specific naming convention and/or approach to  organization scheme. The terminology may be a flat list of controlled vocabulary, a taxonomy  and partonomy, or an ontology (ref: ILX:0777107, RRID:SCR_023499)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema',
         'slot_usage': {'revision_of': {'any_of': [{'range': 'ParcellationTerminology'},
                                                   {'range': 'string'}],
                                        'name': 'revision_of'}}})

    version: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['VersionedNamedThing']} })
    revision_of: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'revision_of',
         'any_of': [{'range': 'ParcellationTerminology'}, {'range': 'string'}],
         'domain_of': ['VersionedNamedThing']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ParcellationTerminology","AnS:ParcellationTerminology"]] = Field(default=["AnS:ParcellationTerminology"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


class ParcellationTermSet(NamedThing):
    """
    A parcellation term set is the set of parcellation terms within a specific parcellation terminology.  A parcellation term set belongs to one and only one parcellation terminology and each parcellation  term in a parcellation terminology belongs to one and only one term set.  If the parcellation terminology is a taxonomy, parcellation term sets can be used to represent  taxonomic ranks. For consistency, if the terminology does not have the notion of taxonomic ranks,  all terms are grouped into a single parcellation term set.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema'})

    part_of_parcellation_terminology: str = Field(default=..., description="""Reference to the parcellation terminology for which the parcellation term set partitions.""", json_schema_extra = { "linkml_meta": {'alias': 'part_of_parcellation_terminology',
         'any_of': [{'range': 'ParcellationTerminology'}, {'range': 'string'}],
         'domain_of': ['ParcellationTermSet']} })
    ordinal: Optional[int] = Field(default=None, description="""Ordinal of the parcellation term set among other term sets within the context of the  associated parcellation terminology.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'ordinal', 'domain_of': ['ParcellationTermSet', 'ParcellationTerm']} })
    has_parent_parcellation_term_set: Optional[str] = Field(default=None, description="""Reference to the parent parcellation term set for which the parcellation term set is a child  (lower taxonomic rank) of.""", json_schema_extra = { "linkml_meta": {'alias': 'has_parent_parcellation_term_set',
         'any_of': [{'range': 'ParcellationTermSet'}, {'range': 'string'}],
         'domain_of': ['ParcellationTermSet']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ParcellationTermSet","AnS:ParcellationTermSet"]] = Field(default=["AnS:ParcellationTermSet"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


class ParcellationTerm(NamedThing):
    """
    A parcellation term is an individual term within a specific parcellation terminology describing a  single anatomical entity by a persistent identifier, name, symbol and description.  A parcellation  term is a unique and exclusive member of a versioned release parcellation terminology. Although term  identifiers must be unique within the context of one versioned release of a parcellation terminology,  they can be reused in different parcellation terminology versions enabling the representation of  terminology updates and modifications over time.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema'})

    symbol: Optional[str] = Field(default=None, description="""Symbol representing a parcellation term.""", json_schema_extra = { "linkml_meta": {'alias': 'symbol', 'domain_of': ['ParcellationTerm']} })
    part_of_parcellation_term_set: str = Field(default=..., description="""Reference to the parcellation term set for which the parcellation term is part of.""", json_schema_extra = { "linkml_meta": {'alias': 'part_of_parcellation_term_set',
         'any_of': [{'range': 'ParcellationTermSet'}, {'range': 'string'}],
         'domain_of': ['ParcellationTerm']} })
    ordinal: Optional[int] = Field(default=None, description="""Ordinal of the parcellation term among other terms within the context of the associated  parcellation terminology.""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'ordinal', 'domain_of': ['ParcellationTermSet', 'ParcellationTerm']} })
    has_parent_parcellation_term: Optional[str] = Field(default=None, description="""Reference to the parent parcellation term for which the parcellation term is a child ( spatially part) of""", json_schema_extra = { "linkml_meta": {'alias': 'has_parent_parcellation_term',
         'any_of': [{'range': 'ParcellationTerm'}, {'range': 'string'}],
         'domain_of': ['ParcellationTerm']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ParcellationTerm","AnS:ParcellationTerm"]] = Field(default=["AnS:ParcellationTerm"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


class ParcellationColorScheme(VersionedNamedThing):
    """
    A parcellation color scheme is a versioned release color palette that can be used to visualize a  parcellation terminology or its related parcellation annotation. A parcellation terminology may  have zero or more parcellation color schemes and each color scheme is in context of a specific  parcellation terminology, where each parcellation term is assigned a hex color value. A parcellation  color scheme is defined as a part of one and only one parcellation terminology.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema',
         'slot_usage': {'revision_of': {'any_of': [{'range': 'ParcellationColorScheme'},
                                                   {'range': 'string'}],
                                        'name': 'revision_of'}}})

    subject_parcellation_terminology: str = Field(default=..., description="""Reference to the parcellation terminology for which the parcellation color scheme is in  context of.""", json_schema_extra = { "linkml_meta": {'alias': 'subject_parcellation_terminology',
         'any_of': [{'range': 'ParcellationTerminology'}, {'range': 'string'}],
         'domain_of': ['ParcellationColorScheme']} })
    version: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['VersionedNamedThing']} })
    revision_of: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'revision_of',
         'any_of': [{'range': 'ParcellationColorScheme'}, {'range': 'string'}],
         'domain_of': ['VersionedNamedThing']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ParcellationColorScheme","AnS:ParcellationColorScheme"]] = Field(default=["AnS:ParcellationColorScheme"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


class ParcellationColorAssignment(ConfiguredBaseModel):
    """
    The parcellation color assignment associates hex color value to a parcellation term within a  versioned release of a color scheme. A parcellation term is uniquely denoted by a parcellation  term identifier and the parcellation terminology it belongs to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema'})

    part_of_parcellation_color_scheme: str = Field(default=..., description="""Reference to the parcellation color scheme for which the color assignment is part of.""", json_schema_extra = { "linkml_meta": {'alias': 'part_of_parcellation_color_scheme',
         'any_of': [{'range': 'ParcellationColorScheme'}, {'range': 'string'}],
         'domain_of': ['ParcellationColorAssignment']} })
    subject_parcellation_term: str = Field(default=..., description="""Reference to the parcellation term identifier for which the color assignment is about.""", json_schema_extra = { "linkml_meta": {'alias': 'subject_parcellation_term',
         'any_of': [{'range': 'ParcellationTerm'}, {'range': 'string'}],
         'domain_of': ['ParcellationColorAssignment', 'ParcellationAnnotationTermMap']} })
    color: Optional[str] = Field(default=None, description="""A string representing to hex triplet code of a color""", json_schema_extra = { "linkml_meta": {'alias': 'color',
         'domain_of': ['ParcellationColorAssignment'],
         'structured_pattern': {'syntax': '{ColorHexTriplet}'}} })


class AnatomicalAnnotationSet(VersionedNamedThing):
    """
    An anatomical annotation set is a versioned release of a set of anatomical annotations anchored  in the same anatomical space that divides the space into distinct segments following some annotation  criteria or parcellation scheme. For example, the anatomical annotation set of 3D image based  reference atlases (e.g. Allen Mouse CCF) can be expressed as a set of label indices of single  multi-valued image annotations or as a set of segmentation masks (ref: ILX:0777108, RRID:SCR_023499)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema',
         'slot_usage': {'revision_of': {'any_of': [{'range': 'AnatomicalAnnotationSet'},
                                                   {'range': 'string'}],
                                        'name': 'revision_of'}}})

    parameterizes: str = Field(default=..., description="""Reference to the anatomical space for which the anatomical annotation set is anchored""", json_schema_extra = { "linkml_meta": {'alias': 'parameterizes',
         'any_of': [{'range': 'AnatomicalSpace'}, {'range': 'string'}],
         'domain_of': ['AnatomicalAnnotationSet']} })
    version: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['VersionedNamedThing']} })
    revision_of: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'revision_of',
         'any_of': [{'range': 'AnatomicalAnnotationSet'}, {'range': 'string'}],
         'domain_of': ['VersionedNamedThing']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/AnatomicalAnnotationSet","AnS:AnatomicalAnnotationSet"]] = Field(default=["AnS:AnatomicalAnnotationSet"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


class ParcellationAnnotation(ConfiguredBaseModel):
    """
    A parcellation annotation defines a specific segment of an anatomical space denoted by an internal  identifier and is a unique and exclusive member of a versioned release anatomical annotation set.  For example, in the case where the anatomical annotation set is a single multi-value image mask (e.g. Allen Mouse CCF), a specific annotation corresponds to a specific label index (internal identifier) in the mask.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema'})

    part_of_anatomical_annotation_set: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'part_of_anatomical_annotation_set',
         'any_of': [{'range': 'AnatomicalAnnotationSet'}, {'range': 'string'}],
         'domain_of': ['ParcellationAnnotation']} })
    internal_identifier: str = Field(default=..., description="""An identifier that uniquely denotes a specific parcellation annotation within the context of an anatomical annotation set""", json_schema_extra = { "linkml_meta": {'alias': 'internal_identifier', 'domain_of': ['ParcellationAnnotation']} })
    voxel_count: Optional[int] = Field(default=None, description="""The number of voxels (3D pixels) spanned by the parcellation annotation (optional).""", ge=0, json_schema_extra = { "linkml_meta": {'alias': 'voxel_count', 'domain_of': ['ParcellationAnnotation']} })


class ParcellationAnnotationTermMap(ConfiguredBaseModel):
    """
    The parcellation annotation term map table defines the relationship between parcellation annotations and parcellation terms.  A parcellation term is uniquely denoted by a parcellation term identifier and the parcellation terminology it belongs to.  A parcellation term can be spatially parameterized by the union of one or more parcellation annotations within a versioned  release of an anatomical annotation set. For example, annotations defining individual cortical layers in cortical region  R (R1, R2/3, R4, etc) can be combined to define the parent region R.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema'})

    subject_parcellation_annotation: Union[ParcellationAnnotation, str] = Field(default=..., description="""Reference to the parcellation annotation that is the subject of the association.""", json_schema_extra = { "linkml_meta": {'alias': 'subject_parcellation_annotation',
         'any_of': [{'range': 'ParcellationAnnotation'}, {'range': 'string'}],
         'domain_of': ['ParcellationAnnotationTermMap']} })
    subject_parcellation_term: str = Field(default=..., description="""Reference to the parcellation term that is the subject of the association.""", json_schema_extra = { "linkml_meta": {'alias': 'subject_parcellation_term',
         'any_of': [{'range': 'ParcellationTerm'}, {'range': 'string'}],
         'domain_of': ['ParcellationColorAssignment', 'ParcellationAnnotationTermMap']} })


class ParcellationAtlas(VersionedNamedThing):
    """
    A parcellation atlas is a versioned release reference used to guide experiments or deal with the spatial relationship between  objects or the location of objects within the context of some anatomical structure. An atlas is minimally defined by a notion  of space (either implicit or explicit) and an annotation set. Reference atlases usually have additional parts that make them  more useful in certain situations, such as a well defined coordinate system, delineations indicating the boundaries of various  regions or cell populations, landmarks, and labels and names to make it easier to communicate about well known and useful  locations (ref: ILX:0777109, RRID:SCR_023499).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/my-org/anatomical-structure-schema',
         'slot_usage': {'revision_of': {'any_of': [{'range': 'ParcellationAtlas'},
                                                   {'range': 'string'}],
                                        'name': 'revision_of'}}})

    has_anatomical_space: str = Field(default=..., description="""Reference to the anatomical space component of the parcellation atlas""", json_schema_extra = { "linkml_meta": {'alias': 'has_anatomical_space',
         'any_of': [{'range': 'AnatomicalSpace'}, {'range': 'string'}],
         'domain_of': ['ParcellationAtlas']} })
    has_anatomical_annotation_set: str = Field(default=..., description="""Reference to the anatomical annotation set component of the parcellation atlas""", json_schema_extra = { "linkml_meta": {'alias': 'has_anatomical_annotation_set',
         'any_of': [{'range': 'AnatomicalAnnotationSet'}, {'range': 'string'}],
         'domain_of': ['ParcellationAtlas']} })
    has_parcellation_terminology: str = Field(default=..., description="""Reference to the parcellation terminology component of the parcellation atlas""", json_schema_extra = { "linkml_meta": {'alias': 'has_parcellation_terminology',
         'any_of': [{'range': 'ParcellationTerminology'}, {'range': 'string'}],
         'domain_of': ['ParcellationAtlas']} })
    specialization_of: Optional[str] = Field(default=None, description="""Reference to the general (non versioned) parcellation atlas for which the parcellation atlas is a specific  version release of.""", json_schema_extra = { "linkml_meta": {'alias': 'specialization_of',
         'any_of': [{'range': 'ParcellationAtlas'}, {'range': 'string'}],
         'domain_of': ['ParcellationAtlas']} })
    version: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['VersionedNamedThing']} })
    revision_of: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'revision_of',
         'any_of': [{'range': 'ParcellationAtlas'}, {'range': 'string'}],
         'domain_of': ['VersionedNamedThing']} })
    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ParcellationAtlas","AnS:ParcellationAtlas"]] = Field(default=["AnS:ParcellationAtlas"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
VersionedNamedThing.model_rebuild()
ImageDataset.model_rebuild()
AnatomicalSpace.model_rebuild()
ParcellationTerminology.model_rebuild()
ParcellationTermSet.model_rebuild()
ParcellationTerm.model_rebuild()
ParcellationColorScheme.model_rebuild()
ParcellationColorAssignment.model_rebuild()
AnatomicalAnnotationSet.model_rebuild()
ParcellationAnnotation.model_rebuild()
ParcellationAnnotationTermMap.model_rebuild()
ParcellationAtlas.model_rebuild()

