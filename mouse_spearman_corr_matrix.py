import json
import pandas as pd
import collections
import numpy as np

def ranks(input):
	seq = sorted(input)
	index = [seq.index(v) for v in input]
	return index

def spearman_rho(a,b):
	n = len(a)
	a, b = ranks(a), ranks(b)
	d_squareds = [(a[i]-b[i])**2 for i in range(0,n)]
	df = n-2
	return 1-6*sum(d_squareds)/(n*(n**2-1))

# with open('allen_data/dev_mouse/raw_dictionary_no_days.txt') as data_file:    
#     data = json.load(data_file)
data = np.loadtxt('allen_data/dev_mouse/autoencoder/encode_24950.txt').tolist()


with open('allen_data/dev_mouse/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

# for key, value in data.items():
# 	data[key] = [item for sublist in value for item in sublist]

print(data)
matrix = []

for i in genes:
	print(i)
	correlations = []
	for j in genes:
		correlations.append(spearman_rho(data[i], data[j]))
	matrix.append(correlations)

print(len(matrix))

df=pd.DataFrame(matrix,columns=genes)
df.index = genes
print(df.shape)

df.to_csv("allen_data/dev_mouse/mouse_corr_spearman_matrix.csv",sep=',', encoding='utf-8')