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
     'description': 'Contains the core types for the Anatomical Structure Schema.',
     'id': 'https://w3id.org/my-org/anatomical-structure-core-schema',
     'imports': ['linkml:types'],
     'name': 'anatomical-structure-core-schema',
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
     'source_file': 'anatomical_structure_core.yaml',
     'title': 'Anatomical Structure Core Schema'} )


class NamedThing(ConfiguredBaseModel):
    """
    Core base entity for Anatomical Structure schema representing an entity with an identifier  name and description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/my-org/anatomical-structure-core-schema'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/NamedThing","AnS:NamedThing"]] = Field(["AnS:NamedThing"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


class VersionedNamedThing(NamedThing):
    """
    Core base entity for Anatomical Structure schema representing an versioned named thing.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/my-org/anatomical-structure-core-schema'})

    version: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'version', 'domain_of': ['VersionedNamedThing']} })
    revision_of: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'revision_of', 'domain_of': ['VersionedNamedThing']} })
    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    name: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['NamedThing']} })
    description: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['NamedThing']} })
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/VersionedNamedThing","AnS:VersionedNamedThing"]] = Field(["AnS:VersionedNamedThing"], json_schema_extra = { "linkml_meta": {'alias': 'category',
         'designates_type': True,
         'domain_of': ['NamedThing'],
         'is_class_field': True} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
VersionedNamedThing.model_rebuild()

