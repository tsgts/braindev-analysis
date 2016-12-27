import numpy as np
import math
import pandas as pd
from collections import Counter
import json

with open('allen_data/dev_mouse/list_of_genes.txt') as data_file:    
    mouse_genes = json.load(data_file)
mouse_genes = [x.upper() for x in list(set(mouse_genes))]

human_genes = pd.read_csv("allen_data/dev_human/normalized_genes/rows_metadata.csv")
human_genes = human_genes["gene_symbol"]

intersection = list(set(mouse_genes) & set(human_genes))

print(len(intersection))

json.dump(intersection,open('allen_data/dev_human/common_genes.txt','w'),indent=4)