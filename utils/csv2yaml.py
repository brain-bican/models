import argparse
import pandas as pd
from pathlib import Path
import yaml


def class_slots(variable_nm, name, value_tp, numeric_tp):
    classes_dict = {"attributes": dict((k,{"description": d}) for k,d in zip(variable_nm, name))}
    for ii, vtp in enumerate(value_tp):
        if vtp == "numeric" and numeric_tp[ii] == "decimal":
            classes_dict["attributes"][variable_nm[ii]]["range"] = "float"
        if vtp == "numeric" and numeric_tp[ii] == "integer":
            classes_dict["attributes"][variable_nm[ii]]["range"] = "integer"
    return classes_dict


def csv2yaml(csv_filename, yaml_filename, head_filename=None):
    """ Convert a csv file to a linkml schema"""
    df = pd.read_csv(csv_filename)
    classes_dict = {}
    if "category" in df.columns:
        dfg = df.groupby("category").agg(lambda x: list(x))
        for row in dfg.iterrows():
            classes_dict[row[0]] = \
                class_slots(variable_nm=row[1]["variable_name"], name=row[1]["name"],
                            value_tp=row[1]["value_type"], numeric_tp=row[1]["numeric_type"])
    else:
        category_name = Path(csv_filename).stem
        classes_dict[category_name] = \
            class_slots(variable_nm=df["variable_name"].tolist(), name=df["name"].tolist(),
                        value_tp=df["value_type"].tolist(), numeric_tp=df["numeric_type"].tolist())

    if head_filename:
        with open(head_filename, 'r') as file:
            head = yaml.safe_load(file)
    else:
        head = None

    with open(yaml_filename, 'w') as file:
        if head:
            yaml.dump(head, file)
        yaml.dump({"classes": classes_dict}, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="input: csv file")
    parser.add_argument("--output", help="output: yaml file")
    parser.add_argument("--header", help="header file: yaml file")
    args = parser.parse_args()
    csv2yaml(args.csv, args.output, args.header)