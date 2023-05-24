import pandas as pd
import os
from pathlib import Path
from translator import readCSV
from models_py.kbmodel import AnnotationCollection, GeneAnnotation


data_files = (Path(__file__).parent / "../source-data")
genomeannots = readCSV(data_files / '20230412_subset_genome_annotation.csv')

for each in genomeannots:
    if each['authority'] =='NCBI' :
        pattern = '*.gff.gz'
    elif each['authority'] == 'Ensembl' or each['authority'] == 'Gencode' :
        pattern = '*.gff3.gz'

    df = pd.read_csv(each['url'], sep='\t', comment = "#", header=None )
    gffcols = ['seqid','source','type','start','end','score','strand','phase','attributes'] # gff columns
    df.columns = gffcols

    # filter the dataframe to only genes
    pred = [x in ['gene','ncRNA_gene','pseudogene'] for x in df['type'] ]
    df_gene = df[pred].copy(deep=True)
    ngene = len(df_gene)
    print("-- number of genes = %d" % ngene )

    # break attributes into components
    if 1 :
        print("-- parse attributes")
        count = 0
        for gindex, grow in df_gene.iterrows() :

            # split attribute string by semicolon
            astr = grow['attributes']
            arr = astr.split(';')

            # break each component into label-value pair and put into a dictionary
            adict = {}
            for att in arr :
                apart = att.split('=')
                adict[apart[0]] = apart[1]

            # add as columns in the dataframe
            for x in adict :
                df_gene.loc[gindex,x] = adict[x]

            count += 1

            if count % 10000 == 0 :
                print(count,ngene)

    # break database crossreference into components
    if each['authority'] == 'NCBI' :

        print("-- parse db crossreference")

        # break Dbxref into its components
        count = 0
        for gindex, grow in df_gene.iterrows() :

            # split Dbxref string by semicolon
            astr = grow['Dbxref']
            arr = astr.split(',')

            # break each component into label-value pair and put into a dictionary
            adict = {}
            for att in arr :
                apart = att.split(':',1)
                adict[apart[0]] = apart[1]

            # add as columns in the dataframe
            for x in adict :
                df_gene.loc[gindex,x] = adict[x]

            count += 1

            if count % 10000 == 0 :
                print(count,ngene)

    print("-- prepare output dataframe and file")
    # prepare output dataframe
    cols = ['genome_annotation_label','gene_identifier_prefix','gene_local_unique_identifier','symbol','name','gene_biotype']
    df_gene['genome_annotation_label'] = each['label']
    df_gene['gene_identifier_prefix'] = each['gene_identifier_prefix']

    # authority specific mapping and transforms
    if each['authority'] == 'NCBI' :
        out_cols = ['genome_annotation_label','gene_identifier_prefix','GeneID','Name','description','gene_biotype']
    elif each['authority'] == 'Ensembl':
        out_cols = ['genome_annotation_label','gene_identifier_prefix','gene_id','Name','description','biotype']

    # create output dataframe
    out_df = df_gene[out_cols]
    out_df.columns = cols

    fname = 'gene_annotation_%s-%s-%s.csv' % (each['authority'], str(each['taxon_local_unique_identifier']), str(each['version']))
    file = os.path.join(data_files, fname)
    out_df.to_csv(file, index=False)

    # TODO: refactor common functionality and these scripts into accepting args of data files
    annots = readCSV(file)
    translatedannots = []
    for each in annots:
        myannotation = GeneAnnotation(id = each['gene_identifier_prefix'].upper().replace('ENE', 'ene') + ':' + each['gene_local_unique_identifier'],
                                      symbol = each['symbol'],
                                      name = each['name'],
                                      referenced_in = each['genome_annotation_label'],
                                      molecular_type = each['gene_biotype'] if each['gene_biotype'] == 'protein_coding' else 'noncoding') #TODO: confirm if noncoding for the rest of the values or parse them as new enum values)
        translatedannots.append(myannotation)

    break # TODO: this only parses first gff file url since it is a huge file and takes a long time to parse, revisit when refactoring through above TODO

myannotations = AnnotationCollection(annotations=translatedannots)