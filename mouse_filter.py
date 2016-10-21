import numpy as np
import math
import pandas as pd
from collections import Counter

expression_data = pd.read_csv("allen_data/dev_mouse/devmouse_histogram_values.csv")
genes = expression_data["gene_acronym"]
gene_counts = Counter(genes)
bad_genes = {k:v for k,v in gene_counts.items() if v<7}
bad_genes = bad_genes.keys()
print(bad_genes)
print(len(bad_genes))

filtered_genes = expression_data[expression_data["gene_acronym"].isin(bad_genes)==False]
filtered_genes.reset_index(drop=True,inplace=True)
print(filtered_genes)