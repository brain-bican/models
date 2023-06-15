import pathlib
import subprocess as sp
import yaml

kbmodel_yaml = pathlib.Path(__file__).parent.resolve() / "../linkml-schema" / "kbmodel.yaml"
kbmodel_diagram = pathlib.Path(__file__).parent.resolve() / "../erdiagram-autogen" / "kbmodel.md"

# reading the yaml schema and getting all names of classes
with kbmodel_yaml.open() as f:
    schema_yaml = yaml.safe_load(f)
classes = schema_yaml["classes"].keys()

# generating the gen-erdiagram command and including all the classes from the yaml file
cmd = ["gen-erdiagram"]

for cl in classes:
    cmd.extend(["-c", f'"{cl}"'])

cmd.extend([str(kbmodel_yaml), ">", str(kbmodel_diagram)])
# running the command: generating the kbmodel diagram
sp.run(" ".join(cmd), check=True, shell=True)


# reading the diagram file and fixing the names with spaces
with kbmodel_diagram.open() as f:
    diagram_txt = f.read()


to_fix_list = [
    "iri type",
    "predicate type",
    "category typeList",
    "label type",
    "narrative text",
    "biological sequence",
    "symbol type"
]

for el in to_fix_list:
    diagram_txt = diagram_txt.replace(el, "_".join(el.split()))

with kbmodel_diagram.open("w") as f:
    f.write(diagram_txt)
