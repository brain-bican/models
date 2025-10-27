```mermaid
erDiagram
SpatialProportions {
    float str  
    float gpe  
    float gpi  
    float sn  
    float adj  
    float sth  
    string id  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    string license  
    string rights  
    string format  
    date creation_date  
    uriorcurieList category  
}
ProvActivity {

}
ProvEntity {

}
DisplayColor {
    string id  
    uriorcurieList xref  
    string color_hex_triplet  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
ColorPalette {
    string id  
    string name  
    string description  
    uriorcurieList xref  
    iri_type iri  
    stringList type  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
MatrixFile {
    stringList content_url  
    uriorcurieList xref  
    string id  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
Abbreviation {
    string id  
    uriorcurieList xref  
    string term  
    string meaning  
    AbbreviationEntityType entity_type  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
CellSpecimen {
    string id  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
ObservationRow {
    uriorcurieList xref  
    string label  
    string id  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
ObservationMatrix {
    stringList content_url  
    uriorcurieList xref  
    string id  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
ObservationMatrixCreationProcess {
    string id  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
Cluster {
    string id  
    string accession_id  
    string name  
    uriorcurieList xref  
    integer number_of_observations  
    iri_type iri  
    stringList type  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
ClusterSet {
    string id  
    string accession_id  
    string name  
    string description  
    uriorcurieList xref  
    date creation_date  
    iri_type iri  
    stringList type  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
ClusteringProcess {
    string id  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
CellTypeTaxon {
    string id  
    string accession_id  
    string name  
    integer order  
    string description  
    uriorcurieList xref  
    integer number_of_cells  
    iri_type iri  
    stringList type  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
CellTypeSet {
    string id  
    string accession_id  
    string name  
    string description  
    integer order  
    uriorcurieList xref  
    CellTypeSetType cell_type_set_type  
    iri_type iri  
    stringList type  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
CellTypeTaxonomy {
    string id  
    date creation_date  
    string accession_id  
    string name  
    string description  
    uriorcurieList xref  
    iri_type iri  
    stringList type  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}
CellTypeTaxonomyCreationProcess {
    string id  
    iri_type iri  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    float information_content  
    uriorcurieList equivalent_identifiers  
    uriorcurieList named_thing_category  
    uriorcurieList category  
}

SpatialProportions ||--|o ProvEntity : "was_derived_from"
SpatialProportions ||--|o ProvActivity : "was_generated_by"
SpatialProportions ||--}o Attribute : "has attribute"
ProvActivity ||--|o ProvEntity : "used"
ProvEntity ||--|o ProvEntity : "was_derived_from"
ProvEntity ||--|o ProvActivity : "was_generated_by"
DisplayColor ||--|o ColorPalette : "part_of_palette"
DisplayColor ||--|o CellTypeTaxon : "is_color_for_taxon"
DisplayColor ||--|o CellTypeSet : "is_color_for_set"
DisplayColor ||--|o ProvEntity : "was_derived_from"
DisplayColor ||--|o ProvActivity : "was_generated_by"
DisplayColor ||--}o Attribute : "has attribute"
ColorPalette ||--|o CellTypeTaxonomy : "is_palette_for"
ColorPalette ||--|o ProvEntity : "was_derived_from"
ColorPalette ||--|o ProvActivity : "was_generated_by"
ColorPalette ||--}o Attribute : "has attribute"
MatrixFile ||--|o ProvEntity : "was_derived_from"
MatrixFile ||--|o ProvActivity : "was_generated_by"
MatrixFile ||--}o Attribute : "has attribute"
Abbreviation ||--}o GeneAnnotation : "denotes_gene_annotation"
Abbreviation ||--}o ParcellationTerm : "denotes_parcellation_term"
Abbreviation ||--}o CellTypeTaxon : "denotes_cell_type"
Abbreviation ||--|o ProvEntity : "was_derived_from"
Abbreviation ||--|o ProvActivity : "was_generated_by"
Abbreviation ||--}o Attribute : "has attribute"
CellSpecimen ||--|o ProvEntity : "was_derived_from"
CellSpecimen ||--|o ProvActivity : "was_generated_by"
CellSpecimen ||--}o Attribute : "has attribute"
ObservationRow ||--|o CellSpecimen : "was_derived_from"
ObservationRow ||--|o ObservationMatrix : "part_of_matrix"
ObservationRow ||--|o MatrixFile : "represented_in"
ObservationRow ||--|o ProvActivity : "was_generated_by"
ObservationRow ||--}o Attribute : "has attribute"
ObservationMatrix ||--|o ObservationMatrixCreationProcess : "was_generated_by"
ObservationMatrix ||--}o CellSpecimen : "was_derived_from"
ObservationMatrix ||--}o MatrixFile : "represented_by"
ObservationMatrix ||--}o GeneAnnotation : "has_variable"
ObservationMatrix ||--}o Attribute : "has attribute"
ObservationMatrixCreationProcess ||--|o ProvEntity : "used"
ObservationMatrixCreationProcess ||--}o Attribute : "has attribute"
Cluster ||--|o ClusterSet : "part_of_set"
Cluster ||--}o ObservationRow : "contains_observation"
Cluster ||--}o CellSpecimen : "contains_sample"
Cluster ||--|o ProvEntity : "was_derived_from"
Cluster ||--|o ProvActivity : "was_generated_by"
Cluster ||--}o Attribute : "has attribute"
ClusterSet ||--|o ClusteringProcess : "was_generated_by"
ClusterSet ||--}o ObservationMatrix : "was_derived_from"
ClusterSet ||--|o ClusterSet : "is_revision_of"
ClusterSet ||--}o Attribute : "has attribute"
ClusteringProcess ||--}o ObservationMatrix : "used"
ClusteringProcess ||--}o Attribute : "has attribute"
CellTypeTaxon ||--|o CellTypeTaxonomy : "part_of_taxonomy"
CellTypeTaxon ||--|o CellTypeTaxon : "has_parent"
CellTypeTaxon ||--}o Abbreviation : "has_abbreviation"
CellTypeTaxon ||--}o Cluster : "contains_cluster"
CellTypeTaxon ||--|o SpatialProportions : "spatial_regional_proportions"
CellTypeTaxon ||--|o SpatialProportions : "spatial_proportions_marmoset"
CellTypeTaxon ||--|o SpatialProportions : "spatial_proportions_macaque"
CellTypeTaxon ||--|o SpatialProportions : "spatial_proportions_human"
CellTypeTaxon ||--}o GeneAnnotation : "curated_markers_to_primates"
CellTypeTaxon ||--}o GeneAnnotation : "curated_markers_to_mouse"
CellTypeTaxon ||--|o ProvEntity : "was_derived_from"
CellTypeTaxon ||--|o ProvActivity : "was_generated_by"
CellTypeTaxon ||--}o Attribute : "has attribute"
CellTypeSet ||--|o CellTypeTaxonomy : "part_of_taxonomy"
CellTypeSet ||--|o CellTypeSet : "has_parent"
CellTypeSet ||--}o Abbreviation : "has_abbreviation"
CellTypeSet ||--}o CellTypeTaxon : "contains_taxon"
CellTypeSet ||--|o ProvEntity : "was_derived_from"
CellTypeSet ||--|o ProvActivity : "was_generated_by"
CellTypeSet ||--}o Attribute : "has attribute"
CellTypeTaxonomy ||--|o CellTypeTaxonomyCreationProcess : "was_generated_by"
CellTypeTaxonomy ||--}o ClusterSet : "was_derived_from"
CellTypeTaxonomy ||--|o CellTypeTaxonomy : "is_revision_of"
CellTypeTaxonomy ||--}o Attribute : "has attribute"
CellTypeTaxonomyCreationProcess ||--}o ClusterSet : "used"
CellTypeTaxonomyCreationProcess ||--}o Attribute : "has attribute"

```

