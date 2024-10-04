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
Checksum {
    DigestType checksum_algorithm  
    string value  
    string id  
    iri type iri  
    uriorcurieList category  
    stringList type  
    label type name  
    narrative text description  
    boolean deprecated  
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
Checksum ||--}o Attribute : "has attribute"

```

