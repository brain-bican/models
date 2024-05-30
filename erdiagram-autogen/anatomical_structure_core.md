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

VersionedNamedThing ||--|o VersionedNamedThing : "revision_of"

```

