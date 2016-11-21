import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import json

expression_data = pd.read_csv("allen_data/dev_mouse/filtered_expression_values.csv")
genes = set(expression_data["gene_acronym"])

matrix = {}

for gene in list(genes)[:10]:
	print(gene)
	#get all rows with the gene symbol
	matching_rows = expression_data[expression_data["gene_acronym"]==gene]
	matching_rows.reset_index(drop=True,inplace=True)

	#adjust the post-birth ages (4,14,28) to days post conception using average gestation period of 19 days
	def age_adjust(age):
		if age in [4.0,14.0,28.0]:
			age += 19
		return age

	#adjust all the ages
	matching_rows["days"] = matching_rows["days"].map(age_adjust)

	#sort from youngest to oldest, with the adjusted ages
	sorted_rows = matching_rows.sort_values("days",axis=0)
	#select only the regions for the pre-pivot
	heatmap_raw = sorted_rows.loc[:,["days","RSP","Tel","PHy","p3","p2","p1","M","PPH","PH","PMH","MH"]]
	heatmap_raw = list(heatmap_raw.values.tolist())
	matrix[gene] = heatmap_raw

print(matrix)