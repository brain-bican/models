import argparse
import pandas as pd
from pathlib import Path
import yaml


SUPPORTED_TYPES = {"text": "string", "integer": "integer", "date": "date", "float": "float",
                   "boolean": "boolean"}
CONVERT_TYPES = {"integer": int}

class YamlDumper(yaml.Dumper):
    def write_line_break(self, data=None):
        super(YamlDumper, self).write_line_break(data)
        if len(self.indents) == 2:  # This checks if we're at the top level of the document
            super(YamlDumper, self).write_line_break()  # Insert an additional line break


def _create_class_entry(df_row):
    """Create a class entry for a given row in the dataframe"""
    variable_names = df_row["LinkML Slot or Attribute Name"]
    class_dict = {}
    if df_row["Definition_Class"]:
        class_dict["description"] = df_row["Definition_Class"]
    if df_row["Inheritance: is_a"]:
        class_dict["is_a"] = df_row["Inheritance: is_a"]
    if df_row["Inheritance: mixin"]:
        class_dict["mixins"] = df_row["Inheritance: mixin"].split(",")
    if df_row["Subsets_Class"]:
        subsets_l = [el.strip() for el in df_row["Subsets_Class"].split(",")]
        class_dict["in_subset"] = subsets_l

    if not pd.isna(df_row["Class Name"]):
        class_dict["attributes"] = \
            dict((k, {"description": d.strip()}) for k,d in zip(variable_names, df_row["Definition"]))
        for ii, dtp in enumerate(df_row["Data Type"]):
            # if data type is valueset, then we need to check for permissible values
            if dtp.lower() == "valueset":
                if df_row['Permissible Values'][ii]:
                    class_dict["attributes"][variable_names[ii]]["range"] = df_row['Permissible Values'][ii].title().replace(" ", "")
                else:
                    raise Exception("No Permissible Value")
            elif SUPPORTED_TYPES[dtp.lower()] != "string":
                class_dict["attributes"][variable_names[ii]]["range"] = SUPPORTED_TYPES[dtp.lower()]
            # checking for aliases
            aliases_l = []
            if df_row["Proposed BICAN Field"][ii].lower() != variable_names[ii].lower():
                aliases_l.append(df_row["Proposed BICAN Field"][ii].strip())
            if df_row["Aliases"][ii]:
                for el in df_row["Aliases"][ii].split(","):
                    if el.strip().lower() not in [variable_names[ii].strip().lower(), df_row["Proposed BICAN Field"][ii].strip().lower()]:
                        aliases_l.append(el.strip())
            if aliases_l:
                class_dict["attributes"][variable_names[ii]]["aliases"] = aliases_l
            # checking for required
            if not df_row["Nullable"][ii]:
                class_dict["attributes"][variable_names[ii]]["required"] = True

    # adding slots_usage if they are any predicate from prov
    if df_row["Predicate"] and not pd.isna(df_row["Class Name"]):
        class_dict["slot_usage"] = {df_row["Predicate"]:  {"range": df_row["Subject"]}}

    return class_dict


def _create_subsets(csv_dirname):
    """Create a dictionary with subsets"""
    df_sub = pd.read_csv(csv_dirname / "subsets.csv")
    # changing float.nan to None
    df_sub = df_sub.applymap(lambda x: None if pd.isna(x) else x)

    subsets_dict = {}
    for row in df_sub.iterrows():
        subsets_dict[row[1]["Name"]] = {}
        if row[1]["Description"]:
            subsets_dict[row[1]["Name"]]["description"] = row[1]["Description"]

    return subsets_dict


def _create_valuesets(csv_dirname):
    """Create a dictionary with valuesets"""
    df_valsets = pd.read_csv(csv_dirname / "valuesets.csv")
    # changing float.nan to None
    df_valsets = df_valsets.applymap(lambda x: None if pd.isna(x) else x)
    dfg_valsets = df_valsets.groupby("ValueSet Name").agg(lambda x: list(x))
    dfg_valsets['Enum Name'] = dfg_valsets.index

    valsets_dict = {}
    for row in dfg_valsets.iterrows():
        enum_nm = row[1]["Enum Name"].title().replace(" ", "")
        valsets_dict[enum_nm] = {"permissible_values": {}}
        for ii, val in enumerate(row[1]["Value"]):
            if row[1]["Value Description"][ii]:
                valsets_dict[enum_nm]["permissible_values"][val] = {"description": row[1]["Value Description"][ii]}
            else:
                valsets_dict[enum_nm]["permissible_values"][val] = None
    return valsets_dict


def csv2yaml(csv_dirname, yaml_filename, templates_dirname=None):
    """ Convert a csv file to a linkml schema"""
    csv_dirname = Path(csv_dirname)
    if templates_dirname:
        templates_dirname = Path(templates_dirname)
    for tab_name in ["slots", "classes", "subsets", "relations"]:
        csv_filename = csv_dirname / f"{tab_name}.csv"
        if not csv_filename.exists():
            raise Exception(f"File {csv_filename} not found")

    # creating dictionary for all the classes
    classes_dict = {}

    # adding classes from the template file
    if templates_dirname and (templates_dirname / "classes_base.yaml").exists():
        with (templates_dirname / "classes_base.yaml").open() as file:
            classes_base = yaml.safe_load(file)
            for key, val in classes_base.items():
                classes_dict[key] = val

    # reading csv with slots
    df_sl = pd.read_csv(csv_dirname / "slots.csv")
    # changing float.nan to None
    df_sl = df_sl.applymap(lambda x: None if pd.isna(x) else x)
    # groupby
    dfg_sl = df_sl.groupby("LinkML Class Name").agg(lambda x: list(x))
    dfg_sl['Class Name'] = dfg_sl.index

    # reading csv with extra info about classes
    df_cl = pd.read_csv(csv_dirname / "classes.csv")
    # changing float.nan to None
    df_cl = df_cl.applymap(lambda x: None if pd.isna(x) else x)
    df_cl = df_cl.set_index('Name')
    df_cl_sl = dfg_sl.join(df_cl, how="outer", rsuffix="_Class")

    # reading csv with info about relations between classes
    df_rel = pd.read_csv(csv_dirname / "relations.csv")
    # changing float.nan to None
    df_rel = df_rel.applymap(lambda x: None if pd.isna(x) else x)
    df_rel = df_rel.set_index('Object')
    # todo: df_rel.rename(inplace=True)
    df_cl_sl_rel = df_cl_sl.join(df_rel, how="left", rsuffix="_Rel")

    # creating additional dictionaries with subsets and valuesets
    subsets_dict = _create_subsets(csv_dirname)
    valsets_dict = _create_valuesets(csv_dirname)

    for row in df_cl_sl_rel.iterrows():
        classes_dict[row[0]] = _create_class_entry(row[1])

    # reading the header file if available
    if templates_dirname and (templates_dirname / "head.yaml").exists():
        with (templates_dirname / "head.yaml").open() as file:
            head = yaml.safe_load(file)
    else:
        head = None

    # writing all the dictionaries to the model yaml file
    with open(yaml_filename, 'w') as file:
        if head:
            yaml.dump(head, file, sort_keys=False)
        file.write("\n\n")
        if subsets_dict:
            yaml.dump({"subsets": subsets_dict}, file, sort_keys=False, Dumper=YamlDumper, default_flow_style=False)
        file.write("\n\n")
        yaml.dump({"classes": classes_dict}, file, sort_keys=False, Dumper=YamlDumper, default_flow_style=False)
        file.write("\n\n")
        yaml.dump({"enums": valsets_dict}, file, sort_keys=False, Dumper=YamlDumper, default_flow_style=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv_dir", help="input: directory with csv files")
    parser.add_argument("--output", help="output: yaml file")
    parser.add_argument("--templates_dir", help="input: directory with linkml templates")
    args = parser.parse_args()
    csv2yaml(args.csv_dir, args.output, args.templates_dir)
