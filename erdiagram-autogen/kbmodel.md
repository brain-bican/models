```mermaid
erDiagram
LibraryPool {
    string tube_avg_size  
    float tube_contents  
    string tube_internal_label  
    string label  
    string created_by_process_id  
    string created_by_process_type  
}
LibraryAliquot {
    integer input_quantity  
    string label  
    string created_by_process_id  
    string created_by_process_type  
}
Library {
    string method  
    datetime creation_date  
    integer avg_size  
    float input_amount  
    string library_prep_pass  
    float quantification_fmol  
    float quantification_ng  
    float quantification_nm  
    string r1_index  
    string r1_sequence  
    string r2_index  
    string r2_sequence  
    string label  
    string created_by_process_id  
    string created_by_process_type  
}
AmplifiedCdna {
    string method  
    float amplified_quantity  
    string pcr_cycles  
    string percent_cdna_longer_than_400bp  
    string rna_amplification_pass_fail  
    string label  
    string created_by_process_id  
    string created_by_process_type  
}
BarcodedCellSample {
    string port_well  
    string sample_quallity_count  
    string label  
    string created_by_process_id  
    string created_by_process_type  
}
EnrichedCellSample {

}
DissociatedCellSample {
    string cell_prep_type  
    string facs_population_plan  
    string label  
    string created_by_process_id  
    string created_by_process_type  
}
TissueSample {
    string roi_plan  
    string region_of_interest_label  
    string label  
    string created_by_process_id  
    string created_by_process_type  
}
BrainSection {
    string barcode  
    integer ordinal  
    string label  
    string created_by_process_id  
    string created_by_process_type  
}
BrainSegment {
    string barcode  
    string anatomical_division  
    string label  
    string created_by_process_id  
    string created_by_process_type  
}
Donor {
    string label  
    SexType sex  
    date date_of_birth  
    date date_of_death  
    integer age_at_death  
    string full_genotype  
    label_type in_taxon_label  
    string id  
    iri_type iri  
    category_typeList category  
    stringList type  
    label_type name  
    narrative_text description  
}
ProcessOutput {
    string label  
    string created_by_process_id  
    string created_by_process_type  
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

Donor ||--}o OrganismTaxon : "in taxon"
Donor ||--}o Attribute : "has attribute"
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

