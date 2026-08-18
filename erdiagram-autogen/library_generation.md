```mermaid
erDiagram
AmplifiedCdna {
    label_type name  
    float amplified_cDNA_quantity_ng  
    amplified_cdna_rna_amplification_pass_fail amplified_cDNA_result  
    float percent_cdna_longer_than_400bp  
    uriorcurieList xref  
    string id  
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
}
BarcodedCellSample {
    label_type name  
    integer number_of_expected_cells  
    uriorcurieList xref  
    string id  
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
}
BrainSlab {
    label_type name  
    uriorcurieList xref  
    string id  
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
}
CdnaAmplification {
    date cDNA_amplification_process_date  
    string cDNA_amplification_set  
    integer pcr_cycles  
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
    uriorcurieList xref  
}
CellBarcoding {
    barcoded_cell_sample_technique cell_barcoding_method  
    string cell_barcoding_process_date  
    integer input_quantity  
    string port_well  
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
    uriorcurieList xref  
}
CellDissociation {
    string cell_dissociation_process_date  
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
    uriorcurieList xref  
}
CellEnrichment {
    string cell_enrichment_process_date  
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
    uriorcurieList xref  
}
DigitalAsset {
    stringList content_url  
    string data_type  
    stringList digest  
    string id  
    label_type name  
    narrative_text description  
    uriorcurieList category  
    date creation_date  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    string format  
    label_type full_name  
    float information_content  
    iri_type iri  
    string license  
    uriorcurieList named_thing_category  
    stringList provided_by  
    string rights  
    label_typeList synonym  
    stringList type  
    uriorcurieList xref  
}
DissectionRoiDelineation {
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
    uriorcurieList xref  
}
DissectionRoiPolygon {
    label_type name  
    uriorcurieList xref  
    string id  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    iri_type iri  
    stringList type  
}
DissociatedCellSample {
    label_type name  
    dissociated_cell_sample_cell_prep_type cell_prep_type  
    dissociated_cell_sample_cell_label_barcode dissociated_cell_oligo_name  
    uriorcurieList xref  
    string id  
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
}
Donor {
    label_type name  
    string age_at_death_description  
    age_at_death_reference_point age_at_death_reference_point  
    age_at_death_unit age_at_death_unit  
    float age_at_death_value  
    sex biological_sex  
    string species  
    uriorcurieList xref  
    string id  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    label_type in_taxon_label  
    float information_content  
    iri_type iri  
    uriorcurieList named_thing_category  
    stringList provided_by  
    label_typeList synonym  
    stringList type  
}
EnrichedCellSample {
    label_type name  
    string enriched_cell_oligo_name  
    string enrichment_population  
    string histone_modification_marker  
    uriorcurieList xref  
    string id  
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
}
EnrichedCellSampleSplitting {
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
    uriorcurieList xref  
}
Library {
    label_type name  
    integer average_size_bp  
    float concentration_nm  
    float library_quantity_ng  
    library_prep_pass_fail library_result  
    float quantity_fmol  
    library_r1_r2_index r1_r2_index  
    uriorcurieList xref  
    string id  
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
}
LibraryAliquot {
    label_type name  
    uriorcurieList xref  
    string id  
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
}
LibraryConstruction {
    float input_quantity_ng  
    library_technique library_construction_method  
    date library_construction_process_date  
    string library_construction_set  
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
    uriorcurieList xref  
}
LibraryPool {
    label_type name  
    string tube_internal_label  
    uriorcurieList xref  
    string id  
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
}
LibraryPooling {
    string process_date  
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
    uriorcurieList xref  
}
ProvActivity {

}
ProvEntity {

}
TissueDissection {
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
    uriorcurieList xref  
}
TissueSample {
    label_type name  
    stringList structure  
    uriorcurieList xref  
    string id  
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
}

AmplifiedCdna ||--|o BarcodedCellSample : "was_derived_from"
AmplifiedCdna ||--|o CdnaAmplification : "was_generated_by"
AmplifiedCdna ||--}o Attribute : "has attribute"
BarcodedCellSample ||--|o CellBarcoding : "was_generated_by"
BarcodedCellSample ||--}o Attribute : "has attribute"
BarcodedCellSample ||--}o ProvEntity : "was_derived_from"
BrainSlab ||--|o ProvActivity : "was_generated_by"
BrainSlab ||--|o ProvEntity : "was_derived_from"
BrainSlab ||--}o Attribute : "has attribute"
CdnaAmplification ||--|o BarcodedCellSample : "used"
CdnaAmplification ||--}o Attribute : "has attribute"
CellBarcoding ||--}o Attribute : "has attribute"
CellBarcoding ||--}o ProvEntity : "used"
CellDissociation ||--}o Attribute : "has attribute"
CellDissociation ||--}o TissueSample : "used"
CellEnrichment ||--}o Attribute : "has attribute"
CellEnrichment ||--}o DissociatedCellSample : "used"
DigitalAsset ||--|o LibraryPool : "was_derived_from"
DigitalAsset ||--|o ProvActivity : "was_generated_by"
DigitalAsset ||--}o Attribute : "has attribute"
DissectionRoiDelineation ||--|o BrainSlab : "used"
DissectionRoiDelineation ||--}o Attribute : "has attribute"
DissectionRoiPolygon ||--|o BrainSlab : "annotates"
DissectionRoiPolygon ||--|o DissectionRoiDelineation : "was_generated_by"
DissectionRoiPolygon ||--|o ProvEntity : "was_derived_from"
DissectionRoiPolygon ||--}o Attribute : "has attribute"
DissociatedCellSample ||--|o CellDissociation : "was_generated_by"
DissociatedCellSample ||--}o Attribute : "has attribute"
DissociatedCellSample ||--}o TissueSample : "was_derived_from"
Donor ||--|o ProvActivity : "was_generated_by"
Donor ||--|o ProvEntity : "was_derived_from"
Donor ||--}o Attribute : "has attribute"
Donor ||--}o OrganismTaxon : "in taxon"
EnrichedCellSample ||--|o ProvActivity : "was_generated_by"
EnrichedCellSample ||--}o Attribute : "has attribute"
EnrichedCellSample ||--}o ProvEntity : "was_derived_from"
EnrichedCellSampleSplitting ||--|o EnrichedCellSample : "used"
EnrichedCellSampleSplitting ||--}o Attribute : "has attribute"
Library ||--|o LibraryConstruction : "was_generated_by"
Library ||--|o ProvEntity : "was_derived_from"
Library ||--}o Attribute : "has attribute"
LibraryAliquot ||--|o Library : "was_derived_from"
LibraryAliquot ||--|o ProvActivity : "was_generated_by"
LibraryAliquot ||--}o Attribute : "has attribute"
LibraryConstruction ||--|o ProvEntity : "used"
LibraryConstruction ||--}o Attribute : "has attribute"
LibraryPool ||--|o LibraryPooling : "was_generated_by"
LibraryPool ||--}o Attribute : "has attribute"
LibraryPool ||--}o LibraryAliquot : "was_derived_from"
LibraryPooling ||--}o Attribute : "has attribute"
LibraryPooling ||--}o LibraryAliquot : "used"
ProvActivity ||--|o ProvEntity : "used"
ProvEntity ||--|o ProvActivity : "was_generated_by"
ProvEntity ||--|o ProvEntity : "was_derived_from"
TissueDissection ||--|o BrainSlab : "used"
TissueDissection ||--|o DissectionRoiPolygon : "was_guided_by"
TissueDissection ||--}o Attribute : "has attribute"
TissueSample ||--|o DissectionRoiPolygon : "dissection_was_guided_by"
TissueSample ||--|o Donor : "was_derived_from"
TissueSample ||--|o TissueDissection : "was_generated_by"
TissueSample ||--}o Attribute : "has attribute"

```

