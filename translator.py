from kbmodel import AnnotationCollection
import yaml
import csv

# read csv data file
annots = []
with open('20230412_subset_gene_annotation.csv') as csvfile:
    annotreader = csv.DictReader(csvfile)
    for row in annotreader:
        annots.append(row)

# map csv to data yaml
with open(r'data.yaml', 'w') as file:
    translatedannots = []
    for each in annots:
        translated = dict()
        translated['id'] = each['gene_identifier_prefix'].upper().replace('ENE', 'ene') + ':' + each['gene_local_unique_identifier']
        translated['symbol'] = each['symbol']
        translated['name'] = each['name']
        translated['synonym'] = [each['genome_annotation_label']]
        translatedannots.append(translated)
    classannots = dict()
    classannots['annotations'] = translatedannots
    yaml.dump(classannots, file)

# load data yaml
with open('data.yaml') as fp:
    data = yaml.safe_load(fp)
myannotations = AnnotationCollection(annotations=data.get("annotations"))