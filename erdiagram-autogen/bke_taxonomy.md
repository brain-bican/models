```mermaid
erDiagram
DisplayColor {
    string id  
    string color_hex_triplet  
    uriorcurieList xref  
    iri_type iri  
    curieList category  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
}
ProvActivity {

}
ProvEntity {

}
ColorPalette {
    string id  
    string name  
    string description  
    uriorcurieList xref  
    iri_type iri  
    curieList category  
    stringList type  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
}
MatrixFile {
    stringList content_url  
    string id  
    iri_type iri  
    curieList category  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
}
Abbreviation {
    string id  
    string term  
    string meaning  
    string entity_type  
    uriorcurieList xref  
    iri_type iri  
    curieList category  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
}
ParcellationTerm {
    string id  
    iri_type iri  
    curieList category  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
}
CellSpecimen {
    string id  
    iri_type iri  
    curieList category  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
}
ObservationRow {
    string label  
    string id  
    iri_type iri  
    curieList category  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
}
ObservationMatrix {
    stringList content_url  
    string id  
    iri_type iri  
    curieList category  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
}
ObservationMatrixCreationProcess {
    string id  
    iri_type iri  
    curieList category  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
}
Cluster {
    string id  
    string accession_id  
    string name  
    integer number_of_observations  
    uriorcurieList xref  
    iri_type iri  
    curieList category  
    stringList type  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
}
ClusterSet {
    string id  
    datetime created_at  
    string accession_id  
    string name  
    string description  
    uriorcurieList xref  
    iri_type iri  
    curieList category  
    stringList type  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
}
ClusteringProcess {
    string id  
    iri_type iri  
    curieList category  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
}
CellTypeTaxon {
    string id  
    string accession_id  
    string name  
    integer order  
    string description  
    integer number_of_cells  
    uriorcurieList xref  
    iri_type iri  
    curieList category  
    stringList type  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
}
CellTypeSet {
    string id  
    string accession_id  
    string name  
    string description  
    string cell_type_set_type  
    integer order  
    uriorcurieList xref  
    iri_type iri  
    curieList category  
    stringList type  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
}
CellTypeTaxonomy {
    string id  
    datetime created_at  
    string accession_id  
    string name  
    string description  
    uriorcurieList xref  
    iri_type iri  
    curieList category  
    stringList type  
    boolean deprecated  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
}
CellTypeTaxonomyCreationProcess {
    string id  
    iri_type iri  
    curieList category  
    stringList type  
    label_type name  
    narrative_text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
}

DisplayColor ||--|o ColorPalette : "part_of_palette"
DisplayColor ||--|o CellTypeTaxon : "is_color_for_taxon"
DisplayColor ||--|o CellTypeSet : "is_color_for_set"
DisplayColor ||--|o ProvEntity : "was_derived_from"
DisplayColor ||--|o ProvActivity : "was_generated_by"
DisplayColor ||--}o Attribute : "has attribute"
ProvActivity ||--|o ProvEntity : "used"
ProvEntity ||--|o ProvEntity : "was_derived_from"
ProvEntity ||--|o ProvActivity : "was_generated_by"
ColorPalette ||--|o CellTypeTaxonomy : "is_palette_for"
ColorPalette ||--|o ProvEntity : "was_derived_from"
ColorPalette ||--|o ProvActivity : "was_generated_by"
ColorPalette ||--}o Attribute : "has attribute"
MatrixFile ||--|o ProvEntity : "was_derived_from"
MatrixFile ||--|o ProvActivity : "was_generated_by"
MatrixFile ||--}o Attribute : "has attribute"
Abbreviation ||--}o GeneAnnotation : "denotes_gene_annotation"
Abbreviation ||--}o ParcellationTerm : "denotes_parcellation_term"
Abbreviation ||--|o ProvEntity : "was_derived_from"
Abbreviation ||--|o ProvActivity : "was_generated_by"
Abbreviation ||--}o Attribute : "has attribute"
ParcellationTerm ||--|o ProvEntity : "was_derived_from"
ParcellationTerm ||--|o ProvActivity : "was_generated_by"
ParcellationTerm ||--}o Attribute : "has attribute"
CellSpecimen ||--|o ProvEntity : "was_derived_from"
CellSpecimen ||--|o ProvActivity : "was_generated_by"
CellSpecimen ||--}o Attribute : "has attribute"
ObservationRow ||--|o ObservationMatrix : "part_of_matrix"
ObservationRow ||--|o MatrixFile : "represented_in"
ObservationRow ||--|o CellSpecimen : "was_derived_from"
ObservationRow ||--|o ProvActivity : "was_generated_by"
ObservationRow ||--}o Attribute : "has attribute"
ObservationMatrix ||--|o ObservationMatrixCreationProcess : "was_generated_by"
ObservationMatrix ||--}o MatrixFile : "represented_by"
ObservationMatrix ||--}o GeneAnnotation : "has_variable"
ObservationMatrix ||--}o CellSpecimen : "was_derived_from"
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
CellTypeTaxon ||--}o Cluster : "contains_cluster"
CellTypeTaxon ||--|o CellTypeTaxon : "has_parent"
CellTypeTaxon ||--}o Abbreviation : "has_abbreviation"
CellTypeTaxon ||--|o ProvEntity : "was_derived_from"
CellTypeTaxon ||--|o ProvActivity : "was_generated_by"
CellTypeTaxon ||--}o Attribute : "has attribute"
CellTypeSet ||--|o CellTypeTaxonomy : "part_of_taxonomy"
CellTypeSet ||--}o CellTypeTaxon : "contains_taxon"
CellTypeSet ||--|o CellTypeSet : "has_parent"
CellTypeSet ||--}o Abbreviation : "has_abbreviation"
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

