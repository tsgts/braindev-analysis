import pandas as pd
import numpy as np
import json
import collections
import math

expression_values = pd.read_csv("allen_data/organoid/pivot_matrix.csv")

print(expression_values)

genes = sorted(list(set(expression_values["gene"])))

json.dump(genes, open("allen_data/organoid/list_of_genes.txt",'w'), indent=4)

matrix = collections.OrderedDict()

for gene in genes:
	print(gene)

	matching_rows = expression_values[expression_values["gene"]==gene]

	matching_rows.reset_index(drop=True,inplace=True)

	#heatmap_raw = matching_rows.loc[:,["timepoint"]+[str(i) for i in range(1,33)]]
	heatmap_raw = matching_rows.loc[:,[str(i) for i in range(1,33)]]
	heatmap_raw = list(heatmap_raw.values.tolist())
	matrix[gene] = heatmap_raw

json.dump(matrix, open("allen_data/organoid/raw_dictionary_no_days.txt",'w'), indent=4)
#json.dump(matrix, open("allen_data/organoid/raw_dictionary.txt",'w'), indent=4)