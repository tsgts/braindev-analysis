import json
import pandas as pd
import collections
from scipy.stats.stats import pearsonr

with open('allen_data/dev_human/raw_dictionary_no_days.txt') as data_file:    
    data = json.load(data_file)

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

for key, value in data.items():
	data[key] = [item for sublist in value for item in sublist]

matrix = []

for i in genes:
	print(i)
	correlations = []
	for j in genes:
		correlations.append(pearsonr(data[i], data[j])[0]**2) 
	matrix.append(correlations)

print(len(matrix))

df=pd.DataFrame(matrix,columns=genes)
print(df.shape)

df.to_csv("allen_data/dev_human/human_raw_corr_pearson_matrix.csv",sep=',', encoding='utf-8')