import pandas as pd
import numpy as np
import json
import collections
import math

expression_values = pd.read_csv("allen_data/dev_human/log_expression_values.csv")

print(expression_values)

genes = sorted(list(set(expression_values["gene"])))

matrix = collections.OrderedDict()

json.dump(genes, open("allen_data/dev_human/list_of_genes.txt",'w'), indent=4)

int_age = {

	"16 pcw": -22,
	"17 pcw": -21,
	"24 pcw": -14,
	"37 pcw": -1,
	"4 mos": 0.33,
	"1 yrs": 1,
	"8 yrs": 8,
	"13 yrs": 13,
	"19 yrs": 19,
	"21 yrs": 21,
	"23 yrs": 23,
	"30 yrs": 30,
	"36 yrs": 36,
	"37 yrs": 37,
	"40 yrs": 40,

}

def safe_log(x):
	if math.isnan(x):
		return -8
	x = float(x)
	if x<=0:
		return -8
	else:
   		return math.log10(x)

for gene in genes:
	print(gene)

	matching_rows = expression_values[expression_values["gene"]==gene]

	matching_rows.reset_index(drop=True,inplace=True)

	def age_adjust(age):
		return int_age[age]

	matching_rows["age"] = matching_rows["age"].map(age_adjust)

	sorted_rows = matching_rows.sort_values("age",axis=0)

	#heatmap_raw = sorted_rows.loc[:,["age","A1C","AMY","CBC","HIP","IPC","MD","OFC","STC","STR","VFC"]]
	heatmap_raw = sorted_rows.loc[:,["A1C","AMY","CBC","HIP","IPC","MD","OFC","STC","STR","VFC"]]
	heatmap_raw = list(heatmap_raw.values.tolist())
	matrix[gene] = heatmap_raw

json.dump(matrix, open("allen_data/dev_human/raw_dictionary_no_days.txt",'w'), indent=4)
#json.dump(matrix, open("allen_data/dev_human/raw_dictionary.txt",'w'), indent=4)