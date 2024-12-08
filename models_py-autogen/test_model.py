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


linkml_meta = LinkMLMeta({'default_prefix': 'bican',
     'default_range': 'string',
     'description': 'The BICAN Prov schema contains a subset of classes from the '
                    'Prov Data Model (PROV-DM) that are frequently used in BICAN '
                    'schemas.',
     'id': 'https://identifiers.org/brain-bican/test-schema',
     'imports': ['linkml:types'],
     'name': 'test-schema',
     'prefixes': {'bican': {'prefix_prefix': 'bican',
                            'prefix_reference': 'https://identifiers.org/brain-bican/vocab/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'test_model.yaml',
     'title': 'Test Schema updated 6'} )


class ProvActivity(ConfiguredBaseModel):
    """
    An activity is something that occurs over a period of time and acts upon or with entities;  it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity',
         'from_schema': 'https://identifiers.org/brain-bican/test-schema',
         'mixin': True})

    used: Optional[str] = Field(None, description="""Usage is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity.""", json_schema_extra = { "linkml_meta": {'alias': 'used', 'domain_of': ['ProvActivity'], 'slot_uri': 'prov:used'} })


class ProvEntity(ConfiguredBaseModel):
    """
    An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects;  entities may be real or imaginary.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity',
         'from_schema': 'https://identifiers.org/brain-bican/test-schema',
         'mixin': True})

    was_derived_from: Optional[str] = Field(None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'alias': 'was_derived_from',
         'domain_of': ['ProvEntity'],
         'slot_uri': 'prov:wasDerivedFrom'} })
    was_generated_by: Optional[str] = Field(None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""", json_schema_extra = { "linkml_meta": {'alias': 'was_generated_by',
         'domain_of': ['ProvEntity'],
         'slot_uri': 'prov:wasGeneratedBy'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ProvActivity.model_rebuild()
ProvEntity.model_rebuild()

