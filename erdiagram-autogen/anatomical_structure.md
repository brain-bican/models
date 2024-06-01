```mermaid
erDiagram
NamedThing {
    uriorcurie id  
    string name  
    string description  
    uriorcurieList category  
}
VersionedNamedThing {
    string version  
    uriorcurie id  
    string name  
    string description  
    uriorcurieList category  
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
    uriorcurie id  
    string name  
    string description  
    uriorcurieList category  
}
AnatomicalSpace {
    string measures  
    string version  
    uriorcurie id  
    string name  
    string description  
    uriorcurieList category  
}
ParcellationTerminology {
    string version  
    uriorcurie id  
    string name  
    string description  
    uriorcurieList category  
}
ParcellationTermSet {
    string part_of_parcellation_terminology  
    integer ordinal  
    string has_parent_parcellation_term_set  
    uriorcurie id  
    string name  
    string description  
    uriorcurieList category  
}
ParcellationTerm {
    string symbol  
    string part_of_parcellation_term_set  
    integer ordinal  
    string has_parent_parcellation_term  
    uriorcurie id  
    string name  
    string description  
    uriorcurieList category  
}
ParcellationColorScheme {
    string subject_parcellation_terminology  
    string version  
    uriorcurie id  
    string name  
    string description  
    uriorcurieList category  
}
ParcellationColorAssignment {
    string part_of_parcellation_color_scheme  
    string subject_parcellation_term  
    string color  
}
AnatomicalAnnotationSet {
    string parameterizes  
    string version  
    uriorcurie id  
    string name  
    string description  
    uriorcurieList category  
}
ParcellationAnnotation {
    string part_of_anatomical_annotation_set  
    string internal_identifier  
    integer voxel_count  
}
ParcellationAnnotationTermMap {
    string subject_parcellation_annotation  
    string subject_parcellation_term  
}
ParcellationAtlas {
    string has_anatomical_space  
    string has_anatomical_annotation_set  
    string has_parcellation_terminology  
    string specialization_of  
    string version  
    uriorcurie id  
    string name  
    string description  
    uriorcurieList category  
}

VersionedNamedThing ||--|o VersionedNamedThing : "revision_of"
ImageDataset ||--|o VersionedNamedThing : "revision_of"
AnatomicalSpace ||--|o VersionedNamedThing : "revision_of"
ParcellationTerminology ||--|o VersionedNamedThing : "revision_of"
ParcellationColorScheme ||--|o VersionedNamedThing : "revision_of"
AnatomicalAnnotationSet ||--|o VersionedNamedThing : "revision_of"
ParcellationAtlas ||--|o VersionedNamedThing : "revision_of"

```

