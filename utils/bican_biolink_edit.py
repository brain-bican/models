# Functions to edit the biolink model after running the general trimmer from bkbit
# Edits are specific to our needs in bican and are not generalizable.
# Earlier the issues were "fixed" by adding "slot_usage", but it might be easier to add it to the bican_biolink directly.
import sys
import yaml
from pathlib import Path

def bican_biolink_edit(schema_yaml: str) -> None:
    """
    Edit the biolink model to fit the bican needs

    :param schema: SchemaView object
    """
    # Change the category slot to have a curie range and a pattern for bican categories
    schema_yaml_path = Path(schema_yaml)
    with schema_yaml_path.open("r") as f:
        schema_dict = yaml.safe_load(f)
    schema_dict["slots"]["category"]["range"] = "curie"
    schema_dict["slots"]["category"]["pattern"] = r"^bican:[A-Z][A-Za-z]+$"
    schema_dict["slots"]["category"]["description"] = schema_dict["slots"]["category"]["description"] + ". NOTE: The category slot was modified to have a curie range and a pattern for bican categories."

    with schema_yaml_path.open("w") as f:
        f.write(yaml.dump(schema_dict, sort_keys=False))


if __name__ == '__main__':
    bican_biolink_yaml_path = sys.argv[1]
    bican_biolink_edit(bican_biolink_yaml_path)