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
    # running the command: generating the kbmodel diagram
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

# 1. FIX GARS DIAGRAM
gars_yaml = pathlib.Path(__file__).parent.resolve() / "../linkml-schema" / "gars.yaml"
gars_diagram = (
    pathlib.Path(__file__).parent.resolve() / "../erdiagram-autogen" / "gars.md"
)
fix_diagram(gars_yaml, gars_diagram)

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
