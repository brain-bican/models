from models_py.kbmodel import AnnotationCollection
import yaml
import csv
from pathlib import Path
import requests
import hashlib

data_files = (Path(__file__).parent / "../source-data")
data_output = (Path(__file__).parent / "../data.yaml")

# read csv data file into a list of dictionaries of data
def readCSV(filename):
    results = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            results.append(row)
    return results

annots = readCSV(data_files / '20230412_subset_gene_annotation.csv')
genomeannots = readCSV(data_files / '20230412_subset_genome_annotation.csv')
genomeassemblies = readCSV(data_files / '20230412_subset_genome_assembly.csv')

def hashBytestrIter(bytesiter, hasher, ashexstr=False):
    for block in bytesiter:
        hasher.update(block)
    return hasher.hexdigest() if ashexstr else hasher.digest()

def fileAsBlockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


# map csv to data yaml
with open(data_output, 'w') as file:
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
        translated['id'] = 'bican:' + each['label']
        if each['taxon_identifier_prefix'] == 'taxonomy':
            translated['in_taxon'] = ['NCBITaxon:' + each['taxon_local_unique_identifier']]
        translated['version'] = each['version']
        translated['description'] = each['description']
        translated['content_url'] = [each['url']]
        r = requests.get(each['url'], allow_redirects=True).content
        m = hashlib.sha256()
        m.update(r)
        translated['digest'] = [m.hexdigest()]
        translatedgenomeannots.append(translated)
    classannots['genome annotations'] = translatedgenomeannots

    translatedassemblies = []
    for each in genomeassemblies:
        translated = dict()
        translated['id'] = each['local_unqiue_identifier']
        if each['taxon_identifier_prefix'] == 'taxonomy':
            translated['taxon'] = 'NCBITaxon:' + each['taxon_local_unique_identifier']
        translated['version'] = each['version']
        translated['label'] = each['label']
        translated['description'] = each['description']
        translatedassemblies.append(translated)
    classannots['genome assemblies'] = translatedassemblies

    yaml.dump(classannots, file)

# load data yaml
with open(data_output) as fp:
    data = yaml.safe_load(fp)
myannotations = AnnotationCollection(annotations=data.get("annotations"))
mygenomeannotations = AnnotationCollection(genome_annotations=data.get("genome annotations"))
mygenomeassemblies = AnnotationCollection(genome_assemblies=data.get("genome assemblies"))