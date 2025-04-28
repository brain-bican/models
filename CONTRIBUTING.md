# Contributing Guildelines

## Checklist for Adding a New LinkML Schema
### 1. create a 'generate_other_formats' github workflow
```
name: generating other formats for <MODEL_NAME>
on:
  pull_request_target:
    types: [opened, synchronize]
    paths:
      - 'linkml-schema/<MODEL_NAME>.yaml'
permissions:
  contents: write
  pull-requests: write
jobs:
  generate_from_reusable:
    uses: brain-bican/models/.github/workflows/reusable-generate_other_formats.yaml@main
    with:
      model_name: <MODEL_NAME>
```

### 2. add schema to generate_docs.yaml github workflow
```
cp erdiagram-autogen/<MODEL_NAME>.md docs/<MODEL_NAME>.md
gen-doc -d docs linkml-schema/<MODEL_NAME>.yaml
mv docs/index.md docs/index_<MODEL_NAME>.md
```

### 3. add schema to software_update_generate_other_formats.yaml github workflow
```
line 19: model_name: genome_annotation, ..., <MODEL_NAME>
```

### 4. add schema to Status Board in README.md


### 5. add schema description to src/docs/index_main.md

### 6. add schema to mkdocs.yml
```
- Models:
    - Library Generation: index_library_generation.md
    .
    .
    .
    - <MODEL_NAME>: index_<MODEL_NAME>.md

- Visualizations:
    - Library Generation: library_generation.md
    .
    .
    .
    - <MODEL_NAME>: <MODEL_NAME>.md
```
      