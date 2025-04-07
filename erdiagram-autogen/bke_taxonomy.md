```mermaid
erDiagram
AnnotationCollection {

}
GenomeAssembly {
    string version  
    string strain  
    label type in_taxon_label  
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
QuantityValue {
    unit has_unit  
    double has_numeric_value  
}
OntologyClass {
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
TaxonomicRank {
    string id  
}
GenomeAnnotation {
    string version  
    stringList digest  
    stringList content_url  
    AuthorityType authority  
    string reference_assembly  
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
GeneAnnotation {
    string molecular_type  
    string source_id  
    string referenced_in  
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

AnnotationCollection ||--}o GeneAnnotation : "annotations"
AnnotationCollection ||--}o GenomeAnnotation : "genome_annotations"
AnnotationCollection ||--}o GenomeAssembly : "genome_assemblies"
GenomeAssembly ||--}o OrganismTaxon : "in taxon"
GenomeAssembly ||--}o Attribute : "has attribute"
Attribute ||--}o Attribute : "has attribute"
Attribute ||--|| OntologyClass : "has attribute type"
Attribute ||--}o QuantityValue : "has quantitative value"
Attribute ||--|o NamedThing : "has qualitative value"
NamedThing ||--}o Attribute : "has attribute"
OrganismTaxon ||--}o Attribute : "has attribute"
OrganismTaxon ||--|o TaxonomicRank : "has taxonomic rank"
GenomeAnnotation ||--}o Attribute : "has attribute"
GenomeAnnotation ||--}o OrganismTaxon : "in taxon"
GeneAnnotation ||--}o Attribute : "has attribute"
GeneAnnotation ||--}o OrganismTaxon : "in taxon"

```

