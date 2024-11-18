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


linkml_meta = LinkMLMeta({'default_prefix': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1/',
     'default_range': 'string',
     'id': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1',
     'imports': ['linkml:types'],
     'name': 'figure1',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'figure1.yaml'} )

class CellCategory(str, Enum):
    NEURON = "NEURON"
    OTHER_IMN = "OTHER_IMN"
    OTHER_VASCULAR = "OTHER_VASCULAR"
    NEUROGLIAL = "NEUROGLIAL"


class BroadRegion(str, Enum):
    PALL = "PALL"
    CNU = "CNU"
    TH = "TH"
    HY = "HY"
    MB = "MB"
    HB = "HB"
    CB = "CB"


class Division(str, Enum):
    Pallium_glutamatergic = "Pallium glutamatergic"
    Subpallium_GABAergic = "Subpallium GABAergic"
    PALMINUS_SIGNsAMYMINUS_SIGNTHMINUS_SIGNHY_MINUS_SIGNMBMINUS_SIGNHB_neuronal = "PAL−sAMY−TH−HY −MB−HB neuronal"
    CBXMINUS_SIGNMOBMINUS_SIGNother_neuronal = "CBX−MOB−other neuronal"
    Neuroglial = "Neuroglial"
    Vascular = "Vascular"
    Immune = "Immune"


class NTType(str, Enum):
    Glut = "Glut"
    GABA = "GABA"
    GlutMINUS_SIGNGABA = "Glut−GABA"
    GABAMINUS_SIGNGlyc = "GABA−Glyc"
    Chol = "Chol"
    Dopa = "Dopa"
    Sero = "Sero"
    Nora = "Nora"
    Hist = "Hist"
    NA = "NA"


class HierarchicalRelationshipType(str, Enum):
    PARENT_OF = "PARENT_OF"
    CHILD_OF = "CHILD_OF"


class GroupRelationshipType(str, Enum):
    CONSISTS_OF = "CONSISTS_OF"
    MEMBER_OF = "MEMBER_OF"



class NamedThing(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1'})

    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    label: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['NamedThing']} })


class CellClass(NamedThing):
    """
    Class division in Figure 1, also found in Supplementary Materials: Table 7
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1'})

    category: CellCategory = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'category', 'domain_of': ['CellClass']} })
    has_hierarchical_relationships: Optional[List[HierarchicalRelationship]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'has_hierarchical_relationships',
         'domain_of': ['CellClass', 'CellSubclass', 'Cluster']} })
    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    label: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['NamedThing']} })


class CellSubclass(NamedThing):
    """
    Subclass division in Figure 1
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1'})

    has_hierarchical_relationships: Optional[List[HierarchicalRelationship]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'has_hierarchical_relationships',
         'domain_of': ['CellClass', 'CellSubclass', 'Cluster']} })
    division: Optional[Division] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'division', 'domain_of': ['CellSubclass']} })
    nt_type: Optional[NTType] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'nt_type', 'domain_of': ['CellSubclass']} })
    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    label: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['NamedThing']} })


class Cluster(NamedThing):
    """
    Cluster in Supplementary Materials: Table 7
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1'})

    has_hierarchical_relationships: Optional[List[HierarchicalRelationship]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'has_hierarchical_relationships',
         'domain_of': ['CellClass', 'CellSubclass', 'Cluster']} })
    has_group_relationships: Optional[List[GroupRelationship]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'has_group_relationships', 'domain_of': ['Cluster', 'Cell']} })
    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    label: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['NamedThing']} })


class Cell(NamedThing):
    """
    Cell, a member of a cluster
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1'})

    has_group_relationships: Optional[List[GroupRelationship]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'has_group_relationships', 'domain_of': ['Cluster', 'Cell']} })
    broad_region: Optional[BroadRegion] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'broad_region', 'domain_of': ['Cell']} })
    id: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['NamedThing']} })
    label: Optional[str] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['NamedThing']} })


class Relationship(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1'})

    related_to: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'related_to', 'domain_of': ['Relationship']} })


class HierarchicalRelationship(Relationship):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1'})

    relationship_type: Optional[HierarchicalRelationshipType] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'relationship_type',
         'domain_of': ['HierarchicalRelationship', 'GroupRelationship']} })
    related_to: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'related_to', 'domain_of': ['Relationship']} })


class GroupRelationship(Relationship):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1'})

    relationship_type: Optional[GroupRelationshipType] = Field(None, json_schema_extra = { "linkml_meta": {'alias': 'relationship_type',
         'domain_of': ['HierarchicalRelationship', 'GroupRelationship']} })
    related_to: str = Field(..., json_schema_extra = { "linkml_meta": {'alias': 'related_to', 'domain_of': ['Relationship']} })


class Container(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.biorxiv.org/content/10.1101/2023.01.22.525049v1',
         'tree_root': True})

    subclasses: Optional[List[CellSubclass]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'subclasses', 'domain_of': ['Container']} })
    classes: Optional[List[CellClass]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'classes', 'domain_of': ['Container']} })
    cells: Optional[List[Cell]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'cells', 'domain_of': ['Container']} })
    clusters: Optional[List[Cluster]] = Field(default_factory=list, json_schema_extra = { "linkml_meta": {'alias': 'clusters', 'domain_of': ['Container']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
CellClass.model_rebuild()
CellSubclass.model_rebuild()
Cluster.model_rebuild()
Cell.model_rebuild()
Relationship.model_rebuild()
HierarchicalRelationship.model_rebuild()
GroupRelationship.model_rebuild()
Container.model_rebuild()

