import argparse
import csv
from linkml.generators.pydanticgen import PydanticGenerator
from linkml_runtime.utils.formatutils import camelcase
from pathlib import Path
import sys
import tempfile
import yaml

NUMERIC_TYPES = ["integer", "float", "number"]


def prop2csvrow(prop, cat_name, default_range=None):
    row_dict = {}
    if cat_name:
        row_dict["category"] = cat_name
    row_dict["variable_name"] = prop["title"]
    row_dict["name"] = prop.get("description", "")
    if prop["type"]:
        if prop["type"] == "array":
            if "type" in prop["items"]:
                row_dict["value_type"] = f'list: {prop["items"]["type"]}'
            elif "$ref" in prop["items"]:
                row_dict["value_type"] = f'list: {prop["items"]["$ref"]}'
            else:
                row_dict["value_type"] = "list"
        else:
            row_dict["value_type"] = prop["type"]
    else:
        raise Exception("No type found for", prop["title"])
        #row_dict["value_type"] = default_range
    # TODO: add support for different type of numerics
    if row_dict["value_type"] in NUMERIC_TYPES:
        row_dict["numeric_type"] = row_dict["value_type"]
    return row_dict


def yaml2csv(yaml_filename, csv_filename, class_name=None):
    """ Convert a linkml schema to a csv file"""
    with open(yaml_filename, 'r') as file:
        yaml_dict = yaml.safe_load(file)

    if class_name:
        if class_name in yaml_dict["classes"]:
            class_name_list = [class_name]
        else:
            raise ValueError(f"{class_name} not found in {yaml_filename}")
    else:
        class_name_list = yaml_dict["classes"]

    # generating pydantic version of the model
    model_ser = PydanticGenerator(yaml_filename).serialize()
    tempdir = tempfile.mkdtemp()
    sys.path.append(tempdir)
    with open(Path(tempdir) / "model_tmp.py", "w") as f:
        f.write(model_ser)
    # loading the pydantic version of the model
    import model_tmp as model_pyd

    class_slots = []
    for cl_nm in class_name_list:
        cl_nm_camel = camelcase(cl_nm)
        print("Processing class:", cl_nm, cl_nm_camel)
        pycl = getattr(model_pyd, cl_nm_camel)
        for nm, prop in pycl.schema()["properties"].items():
            if "title" not in prop:
                continue
            print("Processing property:", nm, prop)
            if len(class_name_list) > 1:
                cat_name = cl_nm
            else:
                cat_name = None
            class_slots.append(prop2csvrow(prop, cat_name=cat_name))

    # if there are more than one class, add the category column
    if len(class_name_list) > 1:
        csv_columns = ["category", "variable_name", "name", "value_type", "numeric_type"]
    else:
        csv_columns = ["variable_name", "name", "value_type", "numeric_type"]

    with open(csv_filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(class_slots)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--yaml", help="input: yaml file")
    parser.add_argument("--output", help="output: csv file")
    parser.add_argument("--class_name", help="name of a specific class")
    args = parser.parse_args()
    yaml2csv(args.yaml, args.output, args.class_name)