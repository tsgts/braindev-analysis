import json
import pandas as pd
import collections
import numpy as np
from scipy.spatial.distance import euclidean

data = np.transpose(np.loadtxt('allen_data/dev_mouse/tsne.txt')).tolist()

with open('allen_data/dev_human/list_of_genes.txt') as data_file:    
    genes = json.load(data_file)

matrix = []

for i in range(0,len(data)):
	print(i)
	correlations = []
	for j in range(0,len(data)):
		correlations.append(euclidean(data[i],data[j])) 
	matrix.append(correlations)

print(len(matrix))

df=pd.DataFrame(matrix,columns=genes)
print(df.shape)

df.to_csv("allen_data/dev_mouse/mouse_encoded_corr_pearson_matrix.csv",sep=',', encoding='utf-8')