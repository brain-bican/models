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


class DigestType(str, Enum):
    SHA1 = "spdx:checksumAlgorithm_sha1"
    MD5 = "spdx:checksumAlgorithm_md5"
    SHA256 = "spdx:checksumAlgorithm_sha256"


class BioType(str, Enum):
    protein_coding = "protein_coding"
    noncoding = "noncoding"


class AuthorityType(str, Enum):
    ENSEMBL = "ENSEMBL"
    NCBI = "NCBI"


class OntologyClass(ConfiguredBaseModel):
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")


class Annotation(ConfiguredBaseModel):
    """
    Biolink Model root class for entity annotations.
    """
    pass


class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
    """
    has_unit: Optional[str] = Field(None, description="""connects a quantity value to a unit""")
    has_numeric_value: Optional[float] = Field(None, description="""connects a quantity value to a number""")


class Entity(ConfiguredBaseModel):
    """
    Root Biolink Model class for all things and informational relationships, real or imagined.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Entity","biolink:Entity"]] = Field(["biolink:Entity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")


class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/NamedThing","biolink:NamedThing"]] = Field(["biolink:NamedThing"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class Attribute(NamedThing, OntologyClass):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    category: List[Literal["https://w3id.org/biolink/vocab/Attribute","biolink:Attribute"]] = Field(["biolink:Attribute"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    attribute_name: Optional[str] = Field(None, description="""The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.""")
    has_attribute_type: str = Field(..., description="""connects an attribute to a class that describes it""")
    has_quantitative_value: Optional[List[QuantityValue]] = Field(None, description="""connects an attribute to a value""")
    has_qualitative_value: Optional[str] = Field(None, description="""connects an attribute to a value""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    name: Optional[str] = Field(None, description="""The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.""")


class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")


class OrganismTaxon(NamedThing):
    """
    A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/OrganismTaxon","biolink:OrganismTaxon"]] = Field(["biolink:OrganismTaxon"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    has_taxonomic_rank: Optional[str] = Field(None)


class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/InformationContentEntity","biolink:InformationContentEntity"]] = Field(["biolink:InformationContentEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")


class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Dataset","biolink:Dataset"]] = Field(["biolink:Dataset"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    license: Optional[str] = Field(None)
    rights: Optional[str] = Field(None)
    format: Optional[str] = Field(None)
    creation_date: Optional[date] = Field(None, description="""date on which an entity was created. This can be applied to nodes or edges""")


class PhysicalEssenceOrOccurrent(ConfiguredBaseModel):
    """
    Either a physical or processual entity.
    """
    pass


class PhysicalEssence(PhysicalEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
    """
    pass


class PhysicalEntity(PhysicalEssence, NamedThing):
    """
    An entity that has material reality (a.k.a. physical essence).
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/PhysicalEntity","biolink:PhysicalEntity"]] = Field(["biolink:PhysicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class Occurrent(PhysicalEssenceOrOccurrent):
    """
    A processual entity.
    """
    pass


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    pass


class Activity(ActivityAndBehavior, NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Activity","biolink:Activity"]] = Field(["biolink:Activity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class Procedure(ActivityAndBehavior, NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Procedure","biolink:Procedure"]] = Field(["biolink:Procedure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class SubjectOfInvestigation(ConfiguredBaseModel):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    pass


class MaterialSample(SubjectOfInvestigation, PhysicalEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/MaterialSample","biolink:MaterialSample"]] = Field(["biolink:MaterialSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class ThingWithTaxon(ConfiguredBaseModel):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes
    """
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")


class BiologicalEntity(ThingWithTaxon, NamedThing):
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/BiologicalEntity","biolink:BiologicalEntity"]] = Field(["biolink:BiologicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")


class GenomicEntity(ConfiguredBaseModel):
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")


class ChemicalEntityOrGeneOrGeneProduct(ConfiguredBaseModel):
    """
    A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
    """
    pass


class MacromolecularMachineMixin(ConfiguredBaseModel):
    """
    A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")


class GeneOrGeneProduct(MacromolecularMachineMixin):
    """
    A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another
    """
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")


class Gene(GeneOrGeneProduct, ChemicalEntityOrGeneOrGeneProduct, GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Gene","biolink:Gene"]] = Field(["biolink:Gene"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")
    symbol: Optional[str] = Field(None, description="""Symbol for a particular thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")


class Genome(GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://w3id.org/biolink/vocab/Genome","biolink:Genome"]] = Field(["biolink:Genome"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")


class GeneAnnotation(Gene):
    """
    An annotation describing the location, boundaries, and functions of  individual genes within a genome annotation.
    """
    molecular_type: Optional[Union[BioType, str]] = Field(None)
    source_id: Optional[str] = Field(None, description="""The authority specific identifier.""")
    referenced_in: Union[GenomeAnnotation, str] = Field(..., description="""The genome annotation that this gene annotation was referenced from.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/GeneAnnotation","bican:GeneAnnotation"]] = Field(["bican:GeneAnnotation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")
    symbol: Optional[str] = Field(None, description="""Symbol for a particular thing""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")


class GenomeAnnotation(Genome):
    """
    Location and nomenclature of genes and all of the coding regions in a genome assembly  and the classification of genes and transcripts into types.
    """
    version: Optional[str] = Field(None)
    digest: Optional[List[Union[Checksum, str]]] = Field(default_factory=list, description="""Stores checksum information.""")
    content_url: Optional[List[str]] = Field(default_factory=list)
    authority: Optional[AuthorityType] = Field(None, description="""The organization responsible for publishing the data.""")
    reference_assembly: Union[GenomeAssembly, str] = Field(..., description="""The reference genome assembly that this genome annotation was created from.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/GenomeAnnotation","bican:GenomeAnnotation"]] = Field(["bican:GenomeAnnotation"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")
    has_biological_sequence: Optional[str] = Field(None, description="""connects a genomic feature to its sequence""")


class GenomeAssembly(ThingWithTaxon, NamedThing):
    """
    Genome assembly to contain version and label information
    """
    version: Optional[str] = Field(None)
    strain: Optional[str] = Field(None, description="""The genetic variant or subtype of a species or organism.""")
    in_taxon: Optional[List[str]] = Field(None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""")
    in_taxon_label: Optional[str] = Field(None, description="""The human readable scientific name for the taxon of the entity.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/GenomeAssembly","bican:GenomeAssembly"]] = Field(["bican:GenomeAssembly"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")
    provided_by: Optional[List[str]] = Field(None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""")
    xref: Optional[List[str]] = Field(default_factory=list, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""")
    full_name: Optional[str] = Field(None, description="""a long-form human readable name for a thing""")
    synonym: Optional[List[str]] = Field(default_factory=list, description="""Alternate human-readable names for a thing""")


class Checksum(Entity):
    """
    Checksum values associated with digital entities.
    """
    checksum_algorithm: Optional[DigestType] = Field(None, description="""The type of cryptographic hash function used to calculate the checksum value.""")
    value: Optional[str] = Field(None, description="""The checksum value obtained from a specific cryotographic hash function.""")
    id: str = Field(..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""")
    iri: Optional[str] = Field(None, description="""An IRI for an entity. This is determined by the id using expansion rules.""")
    category: List[Literal["https://identifiers.org/brain-bican/vocab/Checksum","bican:Checksum"]] = Field(["bican:Checksum"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""")
    type: Optional[List[str]] = Field(default_factory=list)
    name: Optional[str] = Field(None, description="""A human-readable name for an attribute or entity.""")
    description: Optional[str] = Field(None, description="""a human-readable description of an entity""")
    has_attribute: Optional[List[str]] = Field(None, description="""connects any entity to an attribute""")
    deprecated: Optional[bool] = Field(None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""")


class AnnotationCollection(ConfiguredBaseModel):
    annotations: Optional[List[GeneAnnotation]] = Field(default_factory=list)
    genome_annotations: Optional[List[GenomeAnnotation]] = Field(default_factory=list)
    genome_assemblies: Optional[List[GenomeAssembly]] = Field(default_factory=list)


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
OntologyClass.model_rebuild()
Annotation.model_rebuild()
QuantityValue.model_rebuild()
Entity.model_rebuild()
NamedThing.model_rebuild()
Attribute.model_rebuild()
TaxonomicRank.model_rebuild()
OrganismTaxon.model_rebuild()
InformationContentEntity.model_rebuild()
Dataset.model_rebuild()
PhysicalEssenceOrOccurrent.model_rebuild()
PhysicalEssence.model_rebuild()
PhysicalEntity.model_rebuild()
Occurrent.model_rebuild()
ActivityAndBehavior.model_rebuild()
Activity.model_rebuild()
Procedure.model_rebuild()
SubjectOfInvestigation.model_rebuild()
MaterialSample.model_rebuild()
ThingWithTaxon.model_rebuild()
BiologicalEntity.model_rebuild()
GenomicEntity.model_rebuild()
ChemicalEntityOrGeneOrGeneProduct.model_rebuild()
MacromolecularMachineMixin.model_rebuild()
GeneOrGeneProduct.model_rebuild()
Gene.model_rebuild()
Genome.model_rebuild()
GeneAnnotation.model_rebuild()
GenomeAnnotation.model_rebuild()
GenomeAssembly.model_rebuild()
Checksum.model_rebuild()
AnnotationCollection.model_rebuild()

