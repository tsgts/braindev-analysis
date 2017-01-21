import pandas as pd
import json

data = pd.read_csv('allen_data/organoid/organoid.csv')

print(data)

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    human_genes = json.load(data_file)

human_genes = ["cell_id"] + human_genes
human_genes.append("species")

print(human_genes)  

data = data.filter(items=human_genes)
data.to_csv("allen_data/organoid/filtered_genes.csv",sep=',', encoding='utf-8')