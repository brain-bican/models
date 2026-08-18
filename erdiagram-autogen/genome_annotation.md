```mermaid
erDiagram
AnnotationCollection {

}
GeneAnnotation {
    string molecular_type  
    string referenced_in  
    string source_id  
    string id  
    symbol_type name  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    biological_sequence has_biological_sequence  
    label_type in_taxon_label  
    float information_content  
    iri_type iri  
    symbol_type macromolecular_machine_mixin_name  
    uriorcurieList named_thing_category  
    stringList provided_by  
    string symbol  
    label_typeList synonym  
    stringList type  
    uriorcurieList xref  
}
GenomeAnnotation {
    AuthorityType authority  
    stringList content_url  
    stringList digest  
    string reference_assembly  
    string version  
    string id  
    label_type name  
    narrative_text description  
    uriorcurieList category  
    boolean deprecated  
    uriorcurieList equivalent_identifiers  
    label_type full_name  
    biological_sequence has_biological_sequence  
    label_type in_taxon_label  
    float information_content  
    iri_type iri  
    uriorcurieList named_thing_category  
    stringList provided_by  
    label_typeList synonym  
    stringList type  
    uriorcurieList xref  
}
GenomeAssembly {
    string strain  
    string version  
    string id  
    label_type name  
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
    uriorcurieList xref  
}

AnnotationCollection ||--}o GeneAnnotation : "annotations"
AnnotationCollection ||--}o GenomeAnnotation : "genome_annotations"
AnnotationCollection ||--}o GenomeAssembly : "genome_assemblies"
GeneAnnotation ||--}o Attribute : "has attribute"
GeneAnnotation ||--}o OrganismTaxon : "in taxon"
GenomeAnnotation ||--}o Attribute : "has attribute"
GenomeAnnotation ||--}o OrganismTaxon : "in taxon"
GenomeAssembly ||--}o Attribute : "has attribute"
GenomeAssembly ||--}o OrganismTaxon : "in taxon"

```

