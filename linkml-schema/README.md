## `LinkML` schemas for the BICAN project:

### bican_biolink.yaml
The model contains a subset of classes from the [Biolink model](https://biolink.github.io/biolink-model/)
with some small modification to fit the needs of the BICAN project (currently only the `category` slot is modified).

The yaml file can be recreated by running the [LinkML trimmer](https://github.com/brain-bican/bkbit/blob/main/bkbit/model_editors/README.md)
from `bkbit` package.:
```bash
TODO
```
In order to adjust the `category` slot, the following you can run:
```commandline
python ../utils/bican_biolink_edit.py bican_biolink.yaml
```
