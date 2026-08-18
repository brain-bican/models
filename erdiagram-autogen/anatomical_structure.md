```mermaid
erDiagram
AnatomicalAnnotationSet {
    string parameterizes  
    string id  
    label_type name  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    float information_content  
    iri_type iri  
    uriorcurieList named_thing_category  
    stringList provided_by  
    label_typeList synonym  
    stringList type  
    string version  
    uriorcurieList xref  
}
AnatomicalSpace {
    string measures  
    string id  
    label_type name  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    float information_content  
    iri_type iri  
    uriorcurieList named_thing_category  
    stringList provided_by  
    label_typeList synonym  
    stringList type  
    string version  
    uriorcurieList xref  
}
ImageDataset {
    DISTANCE_UNIT unit  
    ANATOMICAL_DIRECTION x_direction  
    float x_resolution  
    integer x_size  
    ANATOMICAL_DIRECTION y_direction  
    float y_resolution  
    integer y_size  
    ANATOMICAL_DIRECTION z_direction  
    float z_resolution  
    integer z_size  
    string id  
    label_type name  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    float information_content  
    iri_type iri  
    uriorcurieList named_thing_category  
    stringList provided_by  
    label_typeList synonym  
    stringList type  
    string version  
    uriorcurieList xref  
}
ParcellationAnnotation {
    string internal_identifier  
    string part_of_anatomical_annotation_set  
    integer voxel_count  
}
ParcellationAnnotationTermMap {
    string subject_parcellation_annotation  
    string subject_parcellation_term  
}
ParcellationAtlas {
    string has_anatomical_annotation_set  
    string has_anatomical_space  
    string has_parcellation_terminology  
    string specialization_of  
    string id  
    label_type name  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    float information_content  
    iri_type iri  
    uriorcurieList named_thing_category  
    stringList provided_by  
    label_typeList synonym  
    stringList type  
    string version  
    uriorcurieList xref  
}
ParcellationColorAssignment {
    string color  
    string part_of_parcellation_color_scheme  
    string subject_parcellation_term  
}
ParcellationColorScheme {
    string subject_parcellation_terminology  
    string id  
    label_type name  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    float information_content  
    iri_type iri  
    uriorcurieList named_thing_category  
    stringList provided_by  
    label_typeList synonym  
    stringList type  
    string version  
    uriorcurieList xref  
}
ParcellationTerm {
    string has_parent_parcellation_term  
    integer ordinal  
    string part_of_parcellation_term_set  
    string symbol  
    string id  
    label_type name  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    float information_content  
    iri_type iri  
    uriorcurieList named_thing_category  
    stringList provided_by  
    label_typeList synonym  
    stringList type  
    string version  
    uriorcurieList xref  
}
ParcellationTermSet {
    string has_parent_parcellation_term_set  
    integer ordinal  
    string part_of_parcellation_terminology  
    string id  
    label_type name  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    float information_content  
    iri_type iri  
    uriorcurieList named_thing_category  
    stringList provided_by  
    label_typeList synonym  
    stringList type  
    string version  
    uriorcurieList xref  
}
ParcellationTerminology {
    string id  
    label_type name  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    float information_content  
    iri_type iri  
    uriorcurieList named_thing_category  
    stringList provided_by  
    label_typeList synonym  
    stringList type  
    string version  
    uriorcurieList xref  
}

AnatomicalAnnotationSet ||--|o VersionedNamedThing : "revision_of"
AnatomicalAnnotationSet ||--}o Attribute : "has attribute"
AnatomicalSpace ||--|o VersionedNamedThing : "revision_of"
AnatomicalSpace ||--}o Attribute : "has attribute"
ImageDataset ||--|o VersionedNamedThing : "revision_of"
ImageDataset ||--}o Attribute : "has attribute"
ParcellationAtlas ||--|o VersionedNamedThing : "revision_of"
ParcellationAtlas ||--}o Attribute : "has attribute"
ParcellationColorScheme ||--|o VersionedNamedThing : "revision_of"
ParcellationColorScheme ||--}o Attribute : "has attribute"
ParcellationTerm ||--|o VersionedNamedThing : "revision_of"
ParcellationTerm ||--}o Attribute : "has attribute"
ParcellationTermSet ||--|o VersionedNamedThing : "revision_of"
ParcellationTermSet ||--}o Attribute : "has attribute"
ParcellationTerminology ||--|o VersionedNamedThing : "revision_of"
ParcellationTerminology ||--}o Attribute : "has attribute"

```

