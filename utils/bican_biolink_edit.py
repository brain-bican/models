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
    # The trimmer writes generation_date without a timezone, which is not a valid
    # xsd:dateTime and fails linkml-lint; it is only metadata, so drop it.
    schema_dict.pop("generation_date", None)

    # Add a SKOS exact-match slot to "organism taxon" so a taxon can be linked to
    # its NCBI Taxonomy term as a *node* rather than a literal (biolink:xref stays
    # as it is: a database identifier, range uriorcurie, serialised as a literal).
    #
    # This is declared here rather than inherited from the OntologyMappable mixin in
    # bican_core, because bican_core imports bican_biolink and not the other way
    # round; linkml-lint runs over each schema on its own, so bican_biolink has to
    # resolve without bican_core. "ontology class" is biolink's own class for a term
    # in an external vocabulary (exact_mappings: owl:Class) and carries the
    # "id" identifier slot, which is what makes the generated JSON-LD context emit
    # "@type": "@id". Keep the name and slot_uri in step with OntologyMappable.
    schema_dict["prefixes"]["skos"] = {
        "prefix_prefix": "skos",
        "prefix_reference": "http://www.w3.org/2004/02/skos/core#",
    }
    schema_dict["slots"]["exact match"] = {
        "name": "exact match",
        "description": (
            "An external concept that is interchangeable with this entity. "
            "Symmetric and transitive, so it chains through third-party mappings."
        ),
        "slot_uri": "skos:exactMatch",
        "range": "ontology class",
        "multivalued": True,
    }
    schema_dict["classes"]["organism taxon"]["slots"].append("exact match")

    with schema_yaml_path.open("w") as f:
        f.write(yaml.dump(schema_dict, sort_keys=False))


if __name__ == '__main__':
    bican_biolink_yaml_path = sys.argv[1]
    bican_biolink_edit(bican_biolink_yaml_path)