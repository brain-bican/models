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
    uriorcurieList category  
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
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
}
NamedThing {
    string id  
    iri type iri  
    uriorcurieList category  
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
    uriorcurieList category  
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
    uriorcurieList category  
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
    uriorcurieList category  
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
    uriorcurieList category  
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
    uriorcurieList category  
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
    uriorcurieList category  
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
    uriorcurieList category  
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
    uriorcurieList category  
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
    uriorcurieList category  
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
    uriorcurieList category  
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
Donor {
    label type name  
    sex biological_sex  
    string age_at_death_description  
    age_at_death_reference_point age_at_death_reference_point  
    age_at_death_unit age_at_death_unit  
    float age_at_death_value  
    string species  
    label type in_taxon_label  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
BrainSlab {
    label type name  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
TissueSample {
    label type name  
    stringList structure  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
DissociatedCellSample {
    label type name  
    dissociated_cell_sample_cell_prep_type cell_prep_type  
    dissociated_cell_sample_cell_label_barcode cell_source_oligo_name  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
EnrichedCellSample {
    label type name  
    string enrichment_population  
    string cell_source_oligo_name  
    string histone_modification_marker  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
BarcodedCellSample {
    label type name  
    integer number_of_expected_cells  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
AmplifiedCdna {
    label type name  
    float quantity_ng  
    amplified_cdna_rna_amplification_pass_fail pass_fail_result  
    float percent_cdna_longer_than_400bp  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
Library {
    label type name  
    integer average_size_bp  
    float concentration_nm  
    library_prep_pass_fail pass_fail_result  
    float quantity_fmol  
    float quantity_ng  
    library_r1_r2_index r1_r2_index  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
LibraryAliquot {
    label type name  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
LibraryPool {
    label type name  
    string local_tube_id  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
DissectionRoiDelineation {
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
TissueDissection {
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
CellDissociation {
    string process_date  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
CellEnrichment {
    string process_date  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
EnrichedCellSampleSplitting {
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
CellBarcoding {
    string port_well  
    integer input_quantity  
    string process_date  
    barcoded_cell_sample_technique method  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
CdnaAmplification {
    integer pcr_cycles  
    date process_date  
    string set  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
LibraryConstruction {
    library_technique method  
    date process_date  
    float input_quantity_ng  
    string set  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
LibraryPooling {
    string process_date  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
    stringList provided_by  
    uriorcurieList xref  
    label type full_name  
    label typeList synonym  
}
DissectionRoiPolygon {
    label type name  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    narrative text description  
    boolean deprecated  
}
ProvActivity {

}
ProvEntity {

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
Donor ||--}o OrganismTaxon : "in taxon"
Donor ||--|o ProvEntity : "was_derived_from"
Donor ||--|o ProvActivity : "was_generated_by"
Donor ||--|o ProvEntity : "annotates"
Donor ||--|o ProvEntity : "dissection_was_guided_by"
Donor ||--}o Attribute : "has attribute"
BrainSlab ||--|o Donor : "was_derived_from"
BrainSlab ||--|o ProvActivity : "was_generated_by"
BrainSlab ||--|o ProvEntity : "annotates"
BrainSlab ||--|o ProvEntity : "dissection_was_guided_by"
BrainSlab ||--}o Attribute : "has attribute"
TissueSample ||--|o Donor : "was_derived_from"
TissueSample ||--|o TissueDissection : "was_generated_by"
TissueSample ||--|o DissectionRoiPolygon : "dissection_was_guided_by"
TissueSample ||--|o ProvEntity : "annotates"
TissueSample ||--}o Attribute : "has attribute"
DissociatedCellSample ||--|o CellDissociation : "was_generated_by"
DissociatedCellSample ||--}o TissueSample : "was_derived_from"
DissociatedCellSample ||--|o ProvEntity : "annotates"
DissociatedCellSample ||--|o ProvEntity : "dissection_was_guided_by"
DissociatedCellSample ||--}o Attribute : "has attribute"
EnrichedCellSample ||--|o ProvActivity : "was_generated_by"
EnrichedCellSample ||--}o ProvEntity : "was_derived_from"
EnrichedCellSample ||--|o ProvEntity : "annotates"
EnrichedCellSample ||--|o ProvEntity : "dissection_was_guided_by"
EnrichedCellSample ||--}o Attribute : "has attribute"
BarcodedCellSample ||--|o CellBarcoding : "was_generated_by"
BarcodedCellSample ||--}o ProvEntity : "was_derived_from"
BarcodedCellSample ||--|o ProvEntity : "annotates"
BarcodedCellSample ||--|o ProvEntity : "dissection_was_guided_by"
BarcodedCellSample ||--}o Attribute : "has attribute"
AmplifiedCdna ||--|o CdnaAmplification : "was_generated_by"
AmplifiedCdna ||--|o BarcodedCellSample : "was_derived_from"
AmplifiedCdna ||--|o ProvEntity : "annotates"
AmplifiedCdna ||--|o ProvEntity : "dissection_was_guided_by"
AmplifiedCdna ||--}o Attribute : "has attribute"
Library ||--|o LibraryConstruction : "was_generated_by"
Library ||--|o ProvEntity : "was_derived_from"
Library ||--|o ProvEntity : "annotates"
Library ||--|o ProvEntity : "dissection_was_guided_by"
Library ||--}o Attribute : "has attribute"
LibraryAliquot ||--|o Library : "was_derived_from"
LibraryAliquot ||--|o ProvActivity : "was_generated_by"
LibraryAliquot ||--|o ProvEntity : "annotates"
LibraryAliquot ||--|o ProvEntity : "dissection_was_guided_by"
LibraryAliquot ||--}o Attribute : "has attribute"
LibraryPool ||--|o LibraryPooling : "was_generated_by"
LibraryPool ||--}o LibraryAliquot : "was_derived_from"
LibraryPool ||--|o ProvEntity : "annotates"
LibraryPool ||--|o ProvEntity : "dissection_was_guided_by"
LibraryPool ||--}o Attribute : "has attribute"
DissectionRoiDelineation ||--|o BrainSlab : "used"
DissectionRoiDelineation ||--|o ProvEntity : "was_guided_by"
DissectionRoiDelineation ||--}o Attribute : "has attribute"
TissueDissection ||--|o DissectionRoiPolygon : "was_guided_by"
TissueDissection ||--|o BrainSlab : "used"
TissueDissection ||--}o Attribute : "has attribute"
CellDissociation ||--}o TissueSample : "used"
CellDissociation ||--|o ProvEntity : "was_guided_by"
CellDissociation ||--}o Attribute : "has attribute"
CellEnrichment ||--}o DissociatedCellSample : "used"
CellEnrichment ||--|o ProvEntity : "was_guided_by"
CellEnrichment ||--}o Attribute : "has attribute"
EnrichedCellSampleSplitting ||--|o EnrichedCellSample : "used"
EnrichedCellSampleSplitting ||--|o ProvEntity : "was_guided_by"
EnrichedCellSampleSplitting ||--}o Attribute : "has attribute"
CellBarcoding ||--}o ProvEntity : "used"
CellBarcoding ||--|o ProvEntity : "was_guided_by"
CellBarcoding ||--}o Attribute : "has attribute"
CdnaAmplification ||--|o BarcodedCellSample : "used"
CdnaAmplification ||--|o ProvEntity : "was_guided_by"
CdnaAmplification ||--}o Attribute : "has attribute"
LibraryConstruction ||--|o ProvEntity : "used"
LibraryConstruction ||--|o ProvEntity : "was_guided_by"
LibraryConstruction ||--}o Attribute : "has attribute"
LibraryPooling ||--}o LibraryAliquot : "used"
LibraryPooling ||--|o ProvEntity : "was_guided_by"
LibraryPooling ||--}o Attribute : "has attribute"
DissectionRoiPolygon ||--|o DissectionRoiDelineation : "was_generated_by"
DissectionRoiPolygon ||--|o BrainSlab : "annotates"
DissectionRoiPolygon ||--|o ProvEntity : "was_derived_from"
DissectionRoiPolygon ||--|o ProvEntity : "dissection_was_guided_by"
DissectionRoiPolygon ||--}o Attribute : "has attribute"
ProvActivity ||--|o ProvEntity : "used"
ProvActivity ||--|o ProvEntity : "was_guided_by"
ProvEntity ||--|o ProvEntity : "was_derived_from"
ProvEntity ||--|o ProvActivity : "was_generated_by"
ProvEntity ||--|o ProvEntity : "annotates"
ProvEntity ||--|o ProvEntity : "dissection_was_guided_by"

```

