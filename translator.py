from kbmodel import AnnotationCollection
import yaml
import csv

# read csv data file into a list of dictionaries of data
def readCSV(filename):
    results = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            results.append(row)
    return results

annots = readCSV('20230412_subset_gene_annotation.csv')
genomeannots = readCSV('20230412_subset_genome_annotation.csv')
genomeassemblies = readCSV('20230412_subset_genome_assembly.csv')

# map csv to data yaml
with open(r'data.yaml', 'w') as file:
    classannots = dict()

    translatedannots = []
    for each in annots:
        translated = dict()
        translated['id'] = each['gene_identifier_prefix'].upper().replace('ENE', 'ene') + ':' + each['gene_local_unique_identifier']
        translated['symbol'] = each['symbol']
        translated['name'] = each['name']
        translated['referenced_in'] = each['genome_annotation_label']
        translated['molecular_type'] = each['gene_biotype']
        translatedannots.append(translated)
    classannots['annotations'] = translatedannots

    translatedgenomeannots = []
    for each in genomeannots:
        translated = dict()
        translated['reference_assembly'] = each['assembly_local_unqiue_identifier']
        translated['id'] = each['label']
        translated['in_taxon'] = [each['authority'].upper() + 'Taxon' + ':' + each['taxon_local_unique_identifier']]
        translated['version'] = each['version']
        translated['description'] = each['description']
        translated['content_url'] = [each['url']]
        # translated['digest'] = each[''] #checksum
        translatedgenomeannots.append(translated)
    classannots['genome annotations'] = translatedgenomeannots

    translatedassemblies = []
    for each in genomeassemblies:
        translated = dict()
        translated['id'] = each['local_unqiue_identifier']
        translated['taxon'] = each['taxon_local_unique_identifier']
        translated['version'] = each['version']
        translated['label'] = each['label']
        translated['description'] = each['description']
        translatedassemblies.append(translated)
    classannots['genome assemblies'] = translatedassemblies

    yaml.dump(classannots, file)

# load data yaml
with open('data.yaml') as fp:
    data = yaml.safe_load(fp)
myannotations = AnnotationCollection(annotations=data.get("annotations"))
mygenomeannotations = AnnotationCollection(genome_annotations=data.get("genome annotations"))
mygenomeassemblies = AnnotationCollection(genome_assemblies=data.get("genome assemblies"))