import pandas as pd
import json

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

binders = pd.read_csv("allen_data/dev_human/dna_binders.txt")

ontology=ontology[ontology["Gene"].isin(genes) == True]

print(ontology.drop_duplicates().reset_index(drop=True))
