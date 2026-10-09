"""Add "@version": 1.1 to a generated JSON-LD context.

Why this is needed
------------------
LinkML writes prefixes whose namespace does not end in a URI gen-delim
(":", "/", "?", "#", "[", "]", "@") as an expanded term definition carrying
"@prefix": true -- every OBO namespace, for instance, ends in "_":

    "NCBITaxon": {"@id": "http://purl.obolibrary.org/obo/NCBITaxon_",
                  "@prefix": true}

But "@prefix" is a JSON-LD 1.1 keyword. A processor running in 1.0 mode
discards it and falls back to guessing "is this a prefix?" from the trailing
character, so "NCBITaxon:9823" is read as an absolute IRI with the scheme
"NCBITaxon" instead of expanding. The result is a plausible-looking node that
joins with nothing, produced silently, with no warning.

Measured across the rdflib versions to hand, same context, same data:

    rdflib 5.0.1   ok
    rdflib 6.1.1   file:///<cwd>/NCBITaxon:9823
    rdflib 6.2.0   ncbitaxon:9823
    rdflib 6.3.2   file:///<cwd>/NCBITaxon:9823
    rdflib 7.0.0   ncbitaxon:9823
    rdflib 7.1.1+  ok    (default processing mode changed to 1.1)

Declaring "@version": 1.1 in the context gives the correct IRI on all of them,
so correctness stops depending on which version a consumer happens to install.

LinkML has no option for this (checked 1.5.0, 1.8.1, 1.8.2, 1.8.6), hence this
post-processing step. Drop it if that ever changes upstream.

Why a script rather than sed
----------------------------
"@context": { occurs more than once per file -- the property-scoped contexts on
enum slots use it too (2 to 16 per model). Only the top-level one should be
touched, and it is distinguished solely by indentation. A pattern that stops
matching after an upstream formatting change would fail silently, which is the
exact failure this whole step exists to prevent, so the match is asserted
instead.
"""

import json
import re
import sys
from pathlib import Path

CONTEXT_LINE = re.compile(r'^(\s*)"@context"\s*:\s*\{\s*$')


def add_context_version(path: Path, version: float = 1.1) -> bool:
    """Insert "@version" into the top-level @context. True if the file changed."""
    text = path.read_text()
    doc = json.loads(text)  # fail early if the generator produced something odd

    context = doc.get("@context")
    if not isinstance(context, dict):
        raise ValueError(f"{path}: no top-level @context object")
    if "@version" in context:
        return False

    lines = text.splitlines(keepends=True)
    matches = [(m.group(1), i) for i, line in enumerate(lines)
               if (m := CONTEXT_LINE.match(line))]
    if not matches:
        raise ValueError(f'{path}: no line matching \'"@context": {{\'')

    # The top-level one is the least indented; the rest are property-scoped.
    outermost = min(len(indent) for indent, _ in matches)
    top = [i for indent, i in matches if len(indent) == outermost]
    if len(top) != 1:
        raise ValueError(f"{path}: expected 1 top-level @context, found {len(top)}")
    at = top[0]

    # Take the indent unit from the first child rather than assuming it.
    child_indent = " " * (outermost + 3)
    if at + 1 < len(lines):
        following = lines[at + 1]
        width = len(following) - len(following.lstrip())
        if following.strip() and width > outermost:
            child_indent = " " * width

    lines.insert(at + 1, f'{child_indent}"@version": {version},\n')
    new_text = "".join(lines)

    new_doc = json.loads(new_text)  # must still be valid JSON
    assert new_doc["@context"].pop("@version") == version
    assert new_doc["@context"] == context, f"{path}: context otherwise changed"
    assert {k: v for k, v in new_doc.items() if k != "@context"} == \
           {k: v for k, v in doc.items() if k != "@context"}

    path.write_text(new_text)
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(f"usage: {sys.argv[0]} <context.jsonld> [...]")
    for arg in sys.argv[1:]:
        p = Path(arg)
        changed = add_context_version(p)
        print(f'{p}: {"added" if changed else "already present"} "@version": 1.1')
