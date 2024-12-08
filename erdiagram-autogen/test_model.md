```mermaid
erDiagram
ProvActivity {

}
ProvEntity {

}

ProvActivity ||--|o ProvEntity : "used"
ProvEntity ||--|o ProvEntity : "was_derived_from"
ProvEntity ||--|o ProvActivity : "was_generated_by"

```

