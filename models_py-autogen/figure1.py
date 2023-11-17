from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, ConfigDict, Field
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra='forbid',
        arbitrary_types_allowed=True,
        use_enum_values = True)


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
    
    id: str = Field(...)
    label: Optional[str] = Field(None)
    

class CellClass(NamedThing):
    """
    Class division in Figure 1, also found in Supplementary Materials: Table 7
    """
    category: CellCategory = Field(...)
    has_hierarchical_relationships: Optional[List[HierarchicalRelationship]] = Field(default_factory=list)
    id: str = Field(...)
    label: Optional[str] = Field(None)
    

class CellSubclass(NamedThing):
    """
    Subclass division in Figure 1
    """
    has_hierarchical_relationships: Optional[List[HierarchicalRelationship]] = Field(default_factory=list)
    division: Optional[Division] = Field(None)
    nt_type: Optional[NTType] = Field(None)
    id: str = Field(...)
    label: Optional[str] = Field(None)
    

class Cluster(NamedThing):
    """
    Cluster in Supplementary Materials: Table 7
    """
    has_hierarchical_relationships: Optional[List[HierarchicalRelationship]] = Field(default_factory=list)
    has_group_relationships: Optional[List[GroupRelationship]] = Field(default_factory=list)
    id: str = Field(...)
    label: Optional[str] = Field(None)
    

class Cell(NamedThing):
    """
    Cell, a member of a cluster
    """
    has_group_relationships: Optional[List[GroupRelationship]] = Field(default_factory=list)
    broad_region: Optional[BroadRegion] = Field(None)
    id: str = Field(...)
    label: Optional[str] = Field(None)
    

class Relationship(ConfiguredBaseModel):
    
    related_to: str = Field(...)
    

class HierarchicalRelationship(Relationship):
    
    relationship_type: Optional[HierarchicalRelationshipType] = Field(None)
    related_to: str = Field(...)
    

class GroupRelationship(Relationship):
    
    relationship_type: Optional[GroupRelationshipType] = Field(None)
    related_to: str = Field(...)
    

class Container(ConfiguredBaseModel):
    
    subclasses: Optional[List[CellSubclass]] = Field(default_factory=list)
    classes: Optional[List[CellClass]] = Field(default_factory=list)
    cells: Optional[List[Cell]] = Field(default_factory=list)
    clusters: Optional[List[Cluster]] = Field(default_factory=list)
    


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

