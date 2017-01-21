import pandas as pd
import json

data = pd.read_csv('allen_data/organoid/filtered_genes.csv',sep="\t")

print(data["cell_id"])