import argparse
import pandas as pd
import yaml

COLUMNS_NAMES = {"Field Name", "Definition/Description", "Data Example", "Identifier/Metadata",
                 "Data Type", "Required/Optional for Analysis", "Required/Optional for Tracking",
                 "Allow Null Value", "Required for Alignment", "SubGroup"}
COLUMNS_NAMES_VALUESET = ['Value Name', 'Field Name', 'Code', 'Description', 'Other Info (TBD)']

SUPPORTED_TYPES = {"text": "string", "integer": "integer", "date": "date", "valueset": ""}
CONVERT_TYPES = {"integer": int}

REQ_SUBSETS = ["Required/Optional for Analysis", "Required/Optional for Tracking", "Required for Alignment"]

def _add_enums(enum_names, enums_df):
    enums_dict = {}
    for model_enum_nm, csv_enum_nm in enum_names.items():
        enum_df = enums_df.get_group(csv_enum_nm)
        enum_dict = {}
        for row in enum_df.iterrows():
            el = row[1]
            enum_dict[el["Value Name"]] = {}
            if el["Description"]:
                enum_dict[el["Value Name"]]["description"] = el["Description"]
        enums_dict[model_enum_nm] = {"permissible_values": enum_dict}
    return enums_dict


def csv2yaml(csv_filename, yaml_filename, enum_filename=None, head_filename=None):
    """ Convert a csv file to a linkml schema"""
    df = pd.read_csv(csv_filename)
    assert set(df.columns) == COLUMNS_NAMES

    dfgb = df.groupby("SubGroup").agg(lambda x: list(x))

    if enum_filename:
        df_enum = pd.read_csv(enum_filename)
        assert set(df_enum.columns) == set(COLUMNS_NAMES_VALUESET)
        enum_names_l = list(df_enum["Field Name"].unique())
        dfgb_enum = df_enum.groupby("Field Name")#.agg(lambda x: list(x))
    else:
        enum_names_l = []

    classes_dict = {}
    enum_names_dict = {}
    for row in dfgb.reset_index().iterrows():
        el = row[1]
        att_dict = {}
        for ii, nm in enumerate(el["Field Name"]):
            if el["Identifier/Metadata"][ii].lower() == "identifier":
                continue
            elif el["Identifier/Metadata"][ii].lower() != "metadata":
                raise Exception("Identifier/Metadata must be either 'identifier' or 'metadata'")
            att_dict[nm] = {"description": el["Definition/Description"][ii]}
            if "not" in el["Allow Null Value"][ii].lower():
                att_dict[nm]["required"] = True # todo: check if this is correct

            if el["Data Type"][ii].lower().startswith("valueset"):
                if ":" in el["Data Type"][ii]:
                    set_name = el["Data Type"][ii].split(":")[1].strip()
                else:
                    set_name = nm.lower()
                if set_name not in enum_names_l:
                    print(f"TODO ERROR: Value set {set_name} not found in {enum_filename}")
                    continue
                    #raise Exception(f"Value set {set_name} not found in {enum_filename}")
                tp = f"{''.join([el.title() for el in set_name.split()])}Enum"
                enum_names_dict[tp] = set_name
            elif el["Data Type"][ii].lower() not in SUPPORTED_TYPES:
                raise Exception(f"Data Type {el['Data Type'][ii]} not supported")
            else:
                tp = SUPPORTED_TYPES[el["Data Type"][ii].lower()]
            if tp:
                att_dict[nm]["range"] = tp
            if tp and tp in CONVERT_TYPES:
                fun_conv = CONVERT_TYPES[tp]
            else:
                fun_conv = lambda x: x
            try:
                att_dict[nm]["examples"] = [{"value": fun_conv(ex.strip())} for ex in el["Data Example"][ii].split("\n")]
            except ValueError:
                print(f"TODO ERROR in {nm}: type: {tp}, value: {el['Data Example'][ii]}")

            subsets_list = []
            for req in REQ_SUBSETS:
                if el[req][ii].lower() == "required":
                    subsets_list.append(f"required_for_{req.split()[-1].lower()}")
            if subsets_list:
                att_dict[nm]["in_subset"] = subsets_list

        classes_dict[el["SubGroup"]] = {"attributes": att_dict}

    if enum_names_dict:
        enums_dict = _add_enums(enum_names_dict, dfgb_enum)

    subsets_dict = {}
    for req in REQ_SUBSETS:
        subsets_dict[f"required_for_{req.split()[-1].lower()}"] = {"description": req}

    if head_filename:
        with open(head_filename, 'r') as file:
            head = yaml.safe_load(file)
    else:
        head = None

    with open(yaml_filename, 'w') as file:
        if head:
            yaml.dump(head, file)
        yaml.dump({"subsets": subsets_dict}, file)
        yaml.dump({"classes": classes_dict}, file)
        if enum_names_dict:
            yaml.dump({"enums": enums_dict}, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="input: csv file")
    parser.add_argument("--enum", help="enum input: csv file")
    parser.add_argument("--output", help="output: yaml file")
    parser.add_argument("--header", help="header file: yaml file")
    args = parser.parse_args()
    csv2yaml(args.csv, args.output, args.enum, args.header)