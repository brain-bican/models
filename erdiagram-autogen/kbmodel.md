```mermaid
erDiagram
LibraryPool {
    integer tube_avg_size  
    float tube_contents  
    string tube_internal_label  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
LibraryPooling {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
LibraryAliquot {
    integer input_quantity  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
LibraryAliquoting {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
Library {
    string method  
    datetime creation_date  
    integer avg_size  
    float input_amount  
    boolean library_prep_pass  
    float quantification_fmol  
    float quantification_ng  
    float quantification_nm  
    string r1_index  
    string r1_sequence  
    string r2_index  
    string r2_sequence  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
LibraryConstruction {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
AmplifiedCdna {
    string method  
    float amplified_quantity  
    integer pcr_cycles  
    float percent_cdna_longer_than_400bp  
    boolean rna_amplification_pass  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
CdnaAmplification {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
BarcodedCellSample {
    string port_well  
    string sample_quality_count  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
CellBarcoding {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
EnrichedCellSample {
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
CellEnrichment {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
DissociatedCellSample {
    string cell_prep_type  
    string facs_population_plan  
    integer number_of_cells_collected  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
CellDissociation {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
TissueSample {
    string roi_plan  
    string region_of_interest_label  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
TissueDissecting {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
BrainSection {
    string barcode  
    integer ordinal  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
BrainSegmentSectioning {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
BrainSegment {
    string barcode  
    string anatomical_division  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
BrainExtraction {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
Donor {
    SexType sex  
    date date_of_birth  
    date date_of_death  
    string age_at_death  
    string full_genotype  
    label_type in_taxon_label  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
Activity {
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
Entity {
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
ProvEntity {

}
ProvActivity {

}
AnnotationCollection {

}
GenomeAssembly {
    string version  
    string strain  
    label_type in_taxon_label  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
GenomeAnnotation {
    uriorcurie reference_assembly  
    string version  
    stringList content_url  
    string authority  
    biological_sequence has_biological_sequence  
    string id  
    label_type in_taxon_label  
    stringList provided_by  
    uriorcurieList xref  
    label_type full_name  
    label_typeList synonym  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
GeneAnnotation {
    BioType molecular_type  
    string source_id  
    string symbol  
    uriorcurieList xref  
    biological_sequence has_biological_sequence  
    string id  
    label_type in_taxon_label  
    stringList provided_by  
    label_type full_name  
    label_typeList synonym  
    iri_type iri  
    category_typeList category  
    stringList type  
    symbol_type name  
    narrative_text description  
}
Checksum {
    DigestType checksum_algorithm  
    string value  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}

LibraryPool ||--}o LibraryAliquot : "wasDerivedFrom"
LibraryPool ||--}o LibraryPooling : "wasGeneratedBy"
LibraryPool ||--}o Attribute : "has attribute"
LibraryPooling ||--}o LibraryAliquot : "used"
LibraryPooling ||--}o LibraryPool : "generated"
LibraryPooling ||--}o Attribute : "has attribute"
LibraryAliquot ||--}o Library : "wasDerivedFrom"
LibraryAliquot ||--}o LibraryAliquoting : "wasGeneratedBy"
LibraryAliquot ||--}o Attribute : "has attribute"
LibraryAliquoting ||--}o Library : "used"
LibraryAliquoting ||--}o LibraryAliquot : "generated"
LibraryAliquoting ||--}o Attribute : "has attribute"
Library ||--}o AmplifiedCdna : "wasDerivedFrom"
Library ||--}o LibraryConstruction : "wasGeneratedBy"
Library ||--}o Attribute : "has attribute"
LibraryConstruction ||--}o AmplifiedCdna : "used"
LibraryConstruction ||--}o Library : "generated"
LibraryConstruction ||--}o Attribute : "has attribute"
AmplifiedCdna ||--}o BarcodedCellSample : "wasDerivedFrom"
AmplifiedCdna ||--}o CdnaAmplification : "wasGeneratedBy"
AmplifiedCdna ||--}o Attribute : "has attribute"
CdnaAmplification ||--}o BarcodedCellSample : "used"
CdnaAmplification ||--}o AmplifiedCdna : "generated"
CdnaAmplification ||--}o Attribute : "has attribute"
BarcodedCellSample ||--}o EnrichedCellSample : "wasDerivedFrom"
BarcodedCellSample ||--}o CellBarcoding : "wasGeneratedBy"
BarcodedCellSample ||--}o Attribute : "has attribute"
CellBarcoding ||--}o EnrichedCellSample : "used"
CellBarcoding ||--}o BarcodedCellSample : "generated"
CellBarcoding ||--}o Attribute : "has attribute"
EnrichedCellSample ||--}o DissociatedCellSample : "wasDerivedFrom"
EnrichedCellSample ||--}o CellEnrichment : "wasGeneratedBy"
EnrichedCellSample ||--}o Attribute : "has attribute"
CellEnrichment ||--}o DissociatedCellSample : "used"
CellEnrichment ||--}o EnrichedCellSample : "generated"
CellEnrichment ||--}o Attribute : "has attribute"
DissociatedCellSample ||--}o TissueSample : "wasDerivedFrom"
DissociatedCellSample ||--}o CellDissociation : "wasGeneratedBy"
DissociatedCellSample ||--}o Attribute : "has attribute"
CellDissociation ||--}o TissueSample : "used"
CellDissociation ||--}o DissociatedCellSample : "generated"
CellDissociation ||--}o Attribute : "has attribute"
TissueSample ||--}o BrainSection : "wasDerivedFrom"
TissueSample ||--}o TissueDissecting : "wasGeneratedBy"
TissueSample ||--}o Attribute : "has attribute"
TissueDissecting ||--}o BrainSection : "used"
TissueDissecting ||--}o TissueSample : "generated"
TissueDissecting ||--}o Attribute : "has attribute"
BrainSection ||--}o BrainSegment : "wasDerivedFrom"
BrainSection ||--}o BrainSegmentSectioning : "wasGeneratedBy"
BrainSection ||--}o Attribute : "has attribute"
BrainSegmentSectioning ||--}o BrainSegment : "used"
BrainSegmentSectioning ||--}o BrainSection : "generated"
BrainSegmentSectioning ||--}o Attribute : "has attribute"
BrainSegment ||--}o Donor : "wasDerivedFrom"
BrainSegment ||--}o BrainExtraction : "wasGeneratedBy"
BrainSegment ||--}o Attribute : "has attribute"
BrainExtraction ||--}o Donor : "used"
BrainExtraction ||--}o BrainSegment : "generated"
BrainExtraction ||--}o Attribute : "has attribute"
Donor ||--}o OrganismTaxon : "in taxon"
Donor ||--}o Entity : "wasDerivedFrom"
Donor ||--}o Activity : "wasGeneratedBy"
Donor ||--}o Attribute : "has attribute"
Activity ||--}o Attribute : "has attribute"
Entity ||--}o Attribute : "has attribute"
ProvEntity ||--}o Entity : "wasDerivedFrom"
ProvEntity ||--}o Activity : "wasGeneratedBy"
ProvActivity ||--}o Entity : "used"
ProvActivity ||--}o Entity : "generated"
AnnotationCollection ||--}o GeneAnnotation : "annotations"
AnnotationCollection ||--}o GenomeAnnotation : "genome_annotations"
AnnotationCollection ||--}o GenomeAssembly : "genome_assemblies"
GenomeAssembly ||--}o OrganismTaxon : "in taxon"
GenomeAssembly ||--}o Attribute : "has attribute"
GenomeAnnotation ||--}| Checksum : "digest"
GenomeAnnotation ||--}o OrganismTaxon : "in taxon"
GenomeAnnotation ||--}o Attribute : "has attribute"
GeneAnnotation ||--|o GenomeAnnotation : "referenced in"
GeneAnnotation ||--}o OrganismTaxon : "in taxon"
GeneAnnotation ||--}o Attribute : "has attribute"
Checksum ||--}o Attribute : "has attribute"

```

