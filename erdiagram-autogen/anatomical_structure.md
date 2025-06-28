```mermaid
erDiagram
OntologyClass {
    string id  
}
Annotation {

}
QuantityValue {
    unit has_unit  
    double has_numeric_value  
}
Attribute {
    string id  
    curieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
    label type attribute_name  
    iri type iri  
    label type name  
}
Entity {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
}
NamedThing {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
TaxonomicRank {
    string id  
}
OrganismTaxon {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
InformationContentEntity {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
    string license  
    string rights  
    string format  
    date creation_date  
}
Dataset {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
    string license  
    string rights  
    string format  
    date creation_date  
}
PhysicalEssenceOrOccurrent {

}
PhysicalEssence {

}
PhysicalEntity {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
Occurrent {

}
ActivityAndBehavior {

}
Activity {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
Procedure {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
SubjectOfInvestigation {

}
MaterialSample {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
ThingWithTaxon {
    label type in_taxon_label  
}
BiologicalEntity {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
    label type in_taxon_label  
}
GenomicEntity {
    biological sequence has_biological_sequence  
}
ChemicalEntityOrGeneOrGeneProduct {

}
MacromolecularMachineMixin {
    label type name  
}
GeneOrGeneProduct {
    label type name  
}
Gene {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    label type full_name  
    label typeList synonym  
    label type in_taxon_label  
    string symbol  
    uriorcurieList xref  
    biological sequence has_biological_sequence  
}
Genome {
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
    label type in_taxon_label  
    biological sequence has_biological_sequence  
}
VersionedNamedThing {
    string version  
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
Checksum {
    DigestType checksum_algorithm  
    string value  
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
}
ImageDataset {
    ANATOMICAL_DIRECTION x_direction  
    ANATOMICAL_DIRECTION y_direction  
    ANATOMICAL_DIRECTION z_direction  
    integer x_size  
    integer y_size  
    integer z_size  
    float x_resolution  
    float y_resolution  
    float z_resolution  
    DISTANCE_UNIT unit  
    string version  
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
AnatomicalSpace {
    string measures  
    string version  
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
ParcellationTerminology {
    string version  
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
ParcellationTermSet {
    integer ordinal  
    string part_of_parcellation_terminology  
    string has_parent_parcellation_term_set  
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
ParcellationTerm {
    string symbol  
    string part_of_parcellation_term_set  
    string has_parent_parcellation_term  
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
ParcellationColorScheme {
    string subject_parcellation_terminology  
    string version  
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
ParcellationColorAssignment {
    string subject_parcellation_term  
    string part_of_parcellation_color_scheme  
    string color  
}
AnatomicalAnnotationSet {
    string parameterizes  
    string version  
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
ParcellationAnnotation {
    string part_of_anatomical_annotation_set  
    string internal_identifier  
    integer voxel_count  
}
ParcellationAnnotationTermMap {
    string subject_parcellation_term  
    string subject_parcellation_annotation  
}
ParcellationAtlas {
    string has_anatomical_space  
    string has_anatomical_annotation_set  
    string has_parcellation_terminology  
    string specialization_of  
    string version  
    string id  
    iri type iri  
    curieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}

Attribute ||--}o Attribute : "has attribute"
Attribute ||--|| OntologyClass : "has attribute type"
Attribute ||--}o QuantityValue : "has quantitative value"
Attribute ||--|o NamedThing : "has qualitative value"
Entity ||--}o Attribute : "has attribute"
NamedThing ||--}o Attribute : "has attribute"
OrganismTaxon ||--}o Attribute : "has attribute"
OrganismTaxon ||--|o TaxonomicRank : "has taxonomic rank"
InformationContentEntity ||--}o Attribute : "has attribute"
Dataset ||--}o Attribute : "has attribute"
PhysicalEntity ||--}o Attribute : "has attribute"
Activity ||--}o Attribute : "has attribute"
Procedure ||--}o Attribute : "has attribute"
MaterialSample ||--}o Attribute : "has attribute"
ThingWithTaxon ||--}o OrganismTaxon : "in taxon"
BiologicalEntity ||--}o Attribute : "has attribute"
BiologicalEntity ||--}o OrganismTaxon : "in taxon"
Gene ||--}o Attribute : "has attribute"
Gene ||--}o OrganismTaxon : "in taxon"
Genome ||--}o Attribute : "has attribute"
Genome ||--}o OrganismTaxon : "in taxon"
VersionedNamedThing ||--|o VersionedNamedThing : "revision_of"
VersionedNamedThing ||--}o Attribute : "has attribute"
Checksum ||--}o Attribute : "has attribute"
ImageDataset ||--|o VersionedNamedThing : "revision_of"
ImageDataset ||--}o Attribute : "has attribute"
AnatomicalSpace ||--|o VersionedNamedThing : "revision_of"
AnatomicalSpace ||--}o Attribute : "has attribute"
ParcellationTerminology ||--|o VersionedNamedThing : "revision_of"
ParcellationTerminology ||--}o Attribute : "has attribute"
ParcellationTermSet ||--}o Attribute : "has attribute"
ParcellationTerm ||--}o Attribute : "has attribute"
ParcellationColorScheme ||--|o VersionedNamedThing : "revision_of"
ParcellationColorScheme ||--}o Attribute : "has attribute"
AnatomicalAnnotationSet ||--|o VersionedNamedThing : "revision_of"
AnatomicalAnnotationSet ||--}o Attribute : "has attribute"
ParcellationAtlas ||--|o VersionedNamedThing : "revision_of"
ParcellationAtlas ||--}o Attribute : "has attribute"

```

