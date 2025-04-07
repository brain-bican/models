import pathlib
import subprocess as sp
import yaml


def fix_diagram(yaml_model: pathlib.Path, diagram: pathlib.Path):
    # reading the yaml schema and getting all names of classes
    with yaml_model.open() as f:
        schema_yaml = yaml.safe_load(f)
    classes = schema_yaml["classes"].keys()

    # generating the gen-erdiagram command and including all the classes from the yaml file
    cmd = ["gen-erdiagram"]

    for cl in classes:
        cmd.extend(["-c", f'"{cl}"'])

    cmd.extend([str(yaml_model), ">", str(diagram)])
    sp.run(" ".join(cmd), check=True, shell=True)

    # reading the diagram file and fixing the names with spaces
    with diagram.open() as f:
        diagram_txt = f.read()

    to_fix_list = [
        "iri type",
        "predicate type",
        "category typeList",
        "label type",
        "narrative text",
        "biological sequence",
        "symbol type",
    ]

    for el in to_fix_list:
        diagram_txt = diagram_txt.replace(el, "_".join(el.split()))

    with diagram.open("w") as f:
        f.write(diagram_txt)


# 1. FIX GENOME ANNOTATION DIAGRAM
genome_annotation_yaml = (
    pathlib.Path(__file__).parent.resolve()
    / "../linkml-schema"
    / "genome_annotation.yaml"
)
genome_annotation_diagram = (
    pathlib.Path(__file__).parent.resolve()
    / "../erdiagram-autogen"
    / "genome_annotation.md"
)
fix_diagram(genome_annotation_yaml, genome_annotation_diagram)

# 2. FIX LIBRARY GENERATION DIAGRAM
libgen_yaml = (
    pathlib.Path(__file__).parent.resolve()
    / "../linkml-schema"
    / "library_generation.yaml"
)
libgen_diagram = (
    pathlib.Path(__file__).parent.resolve()
    / "../erdiagram-autogen"
    / "library_generation.md"
)
fix_diagram(libgen_yaml, libgen_diagram)

# 3. FIX BKE TAXONOMY DIAGRAM
bke_taxonomy_yaml = (
    pathlib.Path(__file__).parent.resolve()
    / "../linkml-schema"
    / "bke_taxonomy.yaml"
)
bke_taxonomy_diagram = (
    pathlib.Path(__file__).parent.resolve()
    / "../erdiagram-autogen"
    / "bke_taxonomy.md"
)
fix_diagram(bke_taxonomy_yaml, bke_taxonomy_diagram)