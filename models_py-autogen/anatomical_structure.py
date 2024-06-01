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
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/NamedThing","AnS:NamedThing"]] = Field(["AnS:NamedThing"])


class VersionedNamedThing(NamedThing):
    """
    Core base entity for Anatomical Structure schema representing an versioned named thing.
    """
    version: str = Field(...)
    revision_of: Optional[str] = Field(None)
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/VersionedNamedThing","AnS:VersionedNamedThing"]] = Field(["AnS:VersionedNamedThing"])


class ImageDataset(VersionedNamedThing):
    """
    An image dataset is versioned release of a multidimensional regular grid of measurements  and metadata required for a morphological representation of an entity such as an anatomical  structure (ref: OBI_0003327, RRID:SCR_006266)
    """
    x_direction: Optional[ANATOMICALDIRECTION] = Field(None, description="""A controlled vocabulary attribute defining the x axis direction in terms of anatomical  direction.""")
    y_direction: Optional[ANATOMICALDIRECTION] = Field(None, description="""A controlled vocabulary attribute defining the y axis direction in terms of anatomical  direction.""")
    z_direction: Optional[ANATOMICALDIRECTION] = Field(None, description="""A controlled vocabulary attribute defining the z axis direction in terms of anatomical  direction.""")
    x_size: Optional[int] = Field(None, description="""The number of pixels/voxels (size) along the x axis.""", ge=1)
    y_size: Optional[int] = Field(None, description="""The number of pixels/voxels (size) along the y axis.""", ge=1)
    z_size: Optional[int] = Field(None, description="""The number of pixels/voxels (size) along the y axis.""", ge=1)
    x_resolution: Optional[float] = Field(None, description="""The resolution (length / pixel) in along the x axis (numerical value part).""")
    y_resolution: Optional[float] = Field(None, description="""The resolution (length / pixel) in along the y axis (numerical value part).""")
    z_resolution: Optional[float] = Field(None, description="""The resolution (length / pixel) in along the z axis (numerical value part).""")
    unit: Optional[DISTANCEUNIT] = Field(None, description="""A controlled vocabulary attribute defining the length unit of the x, y, and z  resolution values.""")
    version: str = Field(...)
    revision_of: Optional[str] = Field(None)
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ImageDataset","AnS:ImageDataset"]] = Field(["AnS:ImageDataset"])


class AnatomicalSpace(VersionedNamedThing):
    """
    An anatomical space is versioned release of a mathematical space with a defined mapping  between the anatomical axes and the mathematical axes. An anatomical space may be defined by  a reference image chosen as the biological reference for an anatomical structure of interest  derived from a single or multiple specimens (ref: ILX:0777106, RRID:SCR_023499)
    """
    measures: str = Field(..., description="""Reference to the specific image dataset used to define the anatomical space.""")
    version: str = Field(...)
    revision_of: Optional[str] = Field(None)
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/AnatomicalSpace","AnS:AnatomicalSpace"]] = Field(["AnS:AnatomicalSpace"])


class ParcellationTerminology(VersionedNamedThing):
    """
    A parcellation terminology is a versioned release set of terms that can be used to label  annotations in an atlas, providing human readability and context and allowing communication  about brain locations and structural properties. Typically, a terminology is a set of  descriptive anatomical terms following a specific naming convention and/or approach to  organization scheme. The terminology may be a flat list of controlled vocabulary, a taxonomy  and partonomy, or an ontology (ref: ILX:0777107, RRID:SCR_023499)
    """
    version: str = Field(...)
    revision_of: Optional[str] = Field(None)
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ParcellationTerminology","AnS:ParcellationTerminology"]] = Field(["AnS:ParcellationTerminology"])


class ParcellationTermSet(NamedThing):
    """
    A parcellation term set is the set of parcellation terms within a specific parcellation terminology.  A parcellation term set belongs to one and only one parcellation terminology and each parcellation  term in a parcellation terminology belongs to one and only one term set.  If the parcellation terminology is a taxonomy, parcellation term sets can be used to represent  taxonomic ranks. For consistency, if the terminology does not have the notion of taxonomic ranks,  all terms are grouped into a single parcellation term set.
    """
    part_of_parcellation_terminology: str = Field(..., description="""Reference to the parcellation terminology for which the parcellation term set partitions.""")
    ordinal: Optional[int] = Field(None, description="""Ordinal of the parcellation term set among other term sets within the context of the  associated parcellation terminology.""", ge=0)
    has_parent_parcellation_term_set: Optional[str] = Field(None, description="""Reference to the parent parcellation term set for which the parcellation term set is a child  (lower taxonomic rank) of.""")
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ParcellationTermSet","AnS:ParcellationTermSet"]] = Field(["AnS:ParcellationTermSet"])


class ParcellationTerm(NamedThing):
    """
    A parcellation term is an individual term within a specific parcellation terminology describing a  single anatomical entity by a persistent identifier, name, symbol and description.  A parcellation  term is a unique and exclusive member of a versioned release parcellation terminology. Although term  identifiers must be unique within the context of one versioned release of a parcellation terminology,  they can be reused in different parcellation terminology versions enabling the representation of  terminology updates and modifications over time.
    """
    symbol: Optional[str] = Field(None, description="""Symbol representing a parcellation term.""")
    part_of_parcellation_term_set: str = Field(..., description="""Reference to the parcellation term set for which the parcellation term is part of.""")
    ordinal: Optional[int] = Field(None, description="""Ordinal of the parcellation term among other terms within the context of the associated  parcellation terminology.""", ge=0)
    has_parent_parcellation_term: Optional[str] = Field(None, description="""Reference to the parent parcellation term for which the parcellation term is a child ( spatially part) of""")
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ParcellationTerm","AnS:ParcellationTerm"]] = Field(["AnS:ParcellationTerm"])


class ParcellationColorScheme(VersionedNamedThing):
    """
    A parcellation color scheme is a versioned release color palette that can be used to visualize a  parcellation terminology or its related parcellation annotation. A parcellation terminology may  have zero or more parcellation color schemes and each color scheme is in context of a specific  parcellation terminology, where each parcellation term is assigned a hex color value. A parcellation  color scheme is defined as a part of one and only one parcellation terminology.
    """
    subject_parcellation_terminology: str = Field(..., description="""Reference to the parcellation terminology for which the parcellation color scheme is in  context of.""")
    version: str = Field(...)
    revision_of: Optional[str] = Field(None)
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ParcellationColorScheme","AnS:ParcellationColorScheme"]] = Field(["AnS:ParcellationColorScheme"])


class ParcellationColorAssignment(ConfiguredBaseModel):
    """
    The parcellation color assignment associates hex color value to a parcellation term within a  versioned release of a color scheme. A parcellation term is uniquely denoted by a parcellation  term identifier and the parcellation terminology it belongs to.
    """
    part_of_parcellation_color_scheme: str = Field(..., description="""Reference to the parcellation color scheme for which the color assignment is part of.""")
    subject_parcellation_term: str = Field(..., description="""Reference to the parcellation term identifier for which the color assignment is about.""")
    color: Optional[str] = Field(None, description="""A string representing to hex triplet code of a color""")


class AnatomicalAnnotationSet(VersionedNamedThing):
    """
    An anatomical annotation set is a versioned release of a set of anatomical annotations anchored  in the same anatomical space that divides the space into distinct segments following some annotation  criteria or parcellation scheme. For example, the anatomical annotation set of 3D image based  reference atlases (e.g. Allen Mouse CCF) can be expressed as a set of label indices of single  multi-valued image annotations or as a set of segmentation masks (ref: ILX:0777108, RRID:SCR_023499)
    """
    parameterizes: str = Field(..., description="""Reference to the anatomical space for which the anatomical annotation set is anchored""")
    version: str = Field(...)
    revision_of: Optional[str] = Field(None)
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/AnatomicalAnnotationSet","AnS:AnatomicalAnnotationSet"]] = Field(["AnS:AnatomicalAnnotationSet"])


class ParcellationAnnotation(ConfiguredBaseModel):
    """
    A parcellation annotation defines a specific segment of an anatomical space denoted by an internal  identifier and is a unique and exclusive member of a versioned release anatomical annotation set.  For example, in the case where the anatomical annotation set is a single multi-value image mask (e.g. Allen Mouse CCF), a specific annotation corresponds to a specific label index (internal identifier) in the mask.
    """
    part_of_anatomical_annotation_set: str = Field(...)
    internal_identifier: str = Field(..., description="""An identifier that uniquely denotes a specific parcellation annotation within the context of an anatomical annotation set""")
    voxel_count: Optional[int] = Field(None, description="""The number of voxels (3D pixels) spanned by the parcellation annotation (optional).""", ge=0)


class ParcellationAnnotationTermMap(ConfiguredBaseModel):
    """
    The parcellation annotation term map table defines the relationship between parcellation annotations and parcellation terms.  A parcellation term is uniquely denoted by a parcellation term identifier and the parcellation terminology it belongs to.  A parcellation term can be spatially parameterized by the union of one or more parcellation annotations within a versioned  release of an anatomical annotation set. For example, annotations defining individual cortical layers in cortical region  R (R1, R2/3, R4, etc) can be combined to define the parent region R.
    """
    subject_parcellation_annotation: Union[ParcellationAnnotation, str] = Field(..., description="""Reference to the parcellation annotation that is the subject of the association.""")
    subject_parcellation_term: str = Field(..., description="""Reference to the parcellation term that is the subject of the association.""")


class ParcellationAtlas(VersionedNamedThing):
    """
    A parcellation atlas is a versioned release reference used to guide experiments or deal with the spatial relationship between  objects or the location of objects within the context of some anatomical structure. An atlas is minimally defined by a notion  of space (either implicit or explicit) and an annotation set. Reference atlases usually have additional parts that make them  more useful in certain situations, such as a well defined coordinate system, delineations indicating the boundaries of various  regions or cell populations, landmarks, and labels and names to make it easier to communicate about well known and useful  locations (ref: ILX:0777109, RRID:SCR_023499).
    """
    has_anatomical_space: str = Field(..., description="""Reference to the anatomical space component of the parcellation atlas""")
    has_anatomical_annotation_set: str = Field(..., description="""Reference to the anatomical annotation set component of the parcellation atlas""")
    has_parcellation_terminology: str = Field(..., description="""Reference to the parcellation terminology component of the parcellation atlas""")
    specialization_of: Optional[str] = Field(None, description="""Reference to the general (non versioned) parcellation atlas for which the parcellation atlas is a specific  version release of.""")
    version: str = Field(...)
    revision_of: Optional[str] = Field(None)
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    category: List[Literal["https://w3id.org/my-org/anatomical-structure-schema/ParcellationAtlas","AnS:ParcellationAtlas"]] = Field(["AnS:ParcellationAtlas"])


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

