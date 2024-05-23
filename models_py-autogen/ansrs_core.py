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


class NamedThing(ConfiguredBaseModel):
    """
    Core base entity for ANSRS schema representing an entity with an identifier  name and description.
    """
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)


class VersionedNamedThing(NamedThing):
    """
    Core base entity for ANSRS schema representing an versioned named thing.
    """
    version: str = Field(...)
    revision_of: Optional[str] = Field(None)
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
VersionedNamedThing.model_rebuild()

