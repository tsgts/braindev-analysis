import pandas as pd
import json

data = pd.read_csv('allen_data/organoid/organoid.txt',sep="\t")

organoid_genes = data.columns.values

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    human_genes = json.load(data_file)
   
intersection = list(set(organoid_genes) & set(human_genes))

print(len(intersection))

json.dump(intersection,open('allen_data/organoid/common_genes.txt','w'),indent=4)